import json
import tomllib
from email.utils import parsedate_to_datetime
from datetime import datetime
from pathlib import Path

import httpx
import pytest

from agentland import AgentLandError
from conftest import API_KEY, error_response, json_response

QID = "00000000-0000-4000-8000-000000000001"
SERVER_TIME = "2026-10-31T12:00:00.000Z"


def replies(*responses):
    queue = list(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        item = queue.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    return handler


def looks_like_time(value: str) -> bool:
    for parse in (datetime.fromisoformat, parsedate_to_datetime):
        try:
            parse(value.replace("Z", "+00:00"))
            return True
        except (ValueError, TypeError, IndexError):
            pass
    return False


def test_idempotency_key_reuse_retry_after_no_client_time(make_client):
    created = {"id": "f1", "p": 0.62}
    client, requests, recorder = make_client(
        replies(
            error_response(503, "unavailable"),
            error_response(429, "rate_limited", headers={"Retry-After": "2"}),
            json_response(201, created, {"X-Server-Time": SERVER_TIME}),
        )
    )
    assert client.forecasts.submit(QID, p=0.62) == created
    assert len(requests) == 3
    keys = {r.headers.get("Idempotency-Key") for r in requests}
    assert len(keys) == 1 and None not in keys
    assert any(w >= 2 for w in recorder.waits[1:])
    for r in requests:
        assert r.method == "POST"
        assert r.url.path == f"/v1/questions/{QID}/forecasts"
        assert json.loads(r.content)["p"] == 0.62
        assert "date" not in r.headers
        for name, value in r.headers.items():
            assert not looks_like_time(value), f"client time leaked in {name}"


def test_gives_up_after_max_retries(make_client):
    client, requests, _ = make_client(replies(*[error_response(503, "unavailable") for _ in range(4)]))
    with pytest.raises(AgentLandError) as info:
        client.forecasts.submit(QID, p=0.5)
    assert len(requests) == 4
    assert info.value.status == 503


def test_400_is_not_retried(make_client):
    client, requests, _ = make_client(replies(error_response(400, "validation_failed")))
    with pytest.raises(AgentLandError) as info:
        client.forecasts.submit(QID, p=2)
    assert len(requests) == 1
    assert info.value.status == 400
    assert info.value.code == "validation_failed"


def test_transport_error_on_get_is_retried(make_client):
    me = {"agent": {"handle": "alpha"}}
    client, requests, _ = make_client(
        replies(httpx.ConnectError("boom"), json_response(200, me, {"X-Server-Time": SERVER_TIME}))
    )
    assert client.me() == me
    assert len(requests) == 2


def test_separate_submits_use_different_keys(make_client):
    client, requests, _ = make_client(lambda r: json_response(201, {"id": "f"}))
    client.forecasts.submit(QID, p=0.1)
    client.forecasts.submit(QID, p=0.2)
    assert requests[0].headers["Idempotency-Key"] != requests[1].headers["Idempotency-Key"]


def test_server_time_and_authorization(make_client):
    times = iter(["2026-10-31T12:00:00.000Z", "2026-10-31T12:00:05.000Z"])
    client, requests, _ = make_client(lambda r: json_response(200, {"agent": {}}, {"X-Server-Time": next(times)}))
    client.me()
    assert client.server_time == "2026-10-31T12:00:00.000Z"
    client.me()
    assert client.server_time == "2026-10-31T12:00:05.000Z"
    assert all(r.headers["Authorization"] == f"Bearer {API_KEY}" for r in requests)


def test_paths_and_methods(make_client):
    client, requests, _ = make_client(lambda r: json_response(200, {"data": [], "next_cursor": None}))
    client.me()
    client.questions.list(status="open", horizon=["hour", "day"])
    client.questions.get(QID)
    client.reflections.add(body="lesson")
    me, listing, get, reflection = requests
    assert (me.method, me.url.path) == ("GET", "/v1/me")
    assert (listing.method, listing.url.path) == ("GET", "/v1/questions")
    assert listing.url.params.get("status") == "open"
    assert listing.url.params.get_list("horizon") == ["hour", "day"]
    assert (get.method, get.url.path) == ("GET", f"/v1/questions/{QID}")
    assert (reflection.method, reflection.url.path) == ("POST", "/v1/me/reflections")
    assert json.loads(reflection.content)["body"] == "lesson"
    assert reflection.headers.get("Idempotency-Key")


def test_declared_dependencies():
    data = tomllib.loads((Path(__file__).resolve().parents[1] / "pyproject.toml").read_text())
    project = data["project"]
    assert project["dependencies"] == ["httpx>=0.23.1,<0.29.0", "attrs>=22.2.0", "python-dateutil>=2.8.0"]
    assert project["optional-dependencies"] == {
        "metaculus": ["forecasting-tools>=0.3.5,<0.4"],
        "sealed": ["pynacl>=1.6.2,<1.7"],
    }
    assert not any("cryptography" in d for d in project["dependencies"])
    assert any(d.startswith("cryptography") for d in data["dependency-groups"]["dev"])
    assert "pynacl==1.6.2" in data["dependency-groups"]["dev"]
