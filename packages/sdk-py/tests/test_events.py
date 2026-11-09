import json

import httpx
import pytest

from agentland import AgentLandError
from conftest import error_response, json_response

PRELUDE = "retry: 5000\nevent: ready\ndata: {}\n\n: hb\n\n"
RESIDENT_ONLY = {"reason": "sse_requires_resident", "poll": "/v1/events/poll"}


def event(eid: str) -> dict:
    return {
        "id": eid,
        "cursor": eid,
        "type": "question.opened",
        "agent_id": None,
        "payload": {"question_id": f"q-{eid}"},
        "created_at": "2026-10-31T12:00:00.000Z",
    }


def frame(eid: str) -> str:
    return f"id: {eid}\nevent: question.opened\ndata: {json.dumps(event(eid))}\n\n"


def sse(text: str) -> httpx.Response:
    return httpx.Response(200, content=text.encode(), headers={"content-type": "text/event-stream"})


def replies(*responses):
    queue = list(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        if not queue:
            raise AssertionError("unexpected request")
        return queue.pop(0)

    return handler


def take(iterable, count: int) -> list[str]:
    ids = []
    for item in iterable:
        ids.append(item["id"])
        if len(ids) == count:
            break
    return ids


def test_last_event_id_resume_and_dedupe(make_client):
    client, requests, _ = make_client(
        replies(
            sse(PRELUDE + frame("e1") + frame("e2")),
            sse(PRELUDE + frame("e2") + frame("e3")),
        )
    )
    assert take(client.events(), 3) == ["e1", "e2", "e3"]
    assert [r.url.path for r in requests] == ["/v1/events", "/v1/events"]
    assert "last-event-id" not in requests[0].headers
    assert requests[1].headers["Last-Event-ID"] == "e2"


def test_sse_requires_resident_switches_to_poll(make_client):
    client, requests, recorder = make_client(
        replies(
            error_response(403, "forbidden", RESIDENT_ONLY),
            json_response(200, {"data": [event("e1"), event("e2")], "next_cursor": "k1"}),
            json_response(200, {"data": [], "next_cursor": "k1"}),
            json_response(200, {"data": [event("e3")], "next_cursor": "k2"}),
        )
    )
    assert take(client.events(), 3) == ["e1", "e2", "e3"]
    assert requests[0].url.path == "/v1/events"
    polls = requests[1:]
    assert all(r.url.path == "/v1/events/poll" for r in polls)
    assert "since" not in polls[0].url.params
    assert polls[1].url.params["since"] == "k1"
    assert polls[2].url.params["since"] == "k1"
    assert recorder.waits, "empty poll page must sleep through the injected sleep"


def test_empty_poll_yields_nothing_synthetic(make_client):
    pages = iter(
        [error_response(403, "forbidden", RESIDENT_ONLY)]
        + [json_response(200, {"data": [], "next_cursor": "k0"}) for _ in range(3)]
    )

    def handler(request):
        try:
            return next(pages)
        except StopIteration:
            raise httpx.ConnectError("stop") from None

    client, requests, recorder = make_client(handler, max_retries=0)
    with pytest.raises((httpx.TransportError, AgentLandError)):
        for item in client.events():
            raise AssertionError(f"synthetic event yielded: {item!r}")
    assert len(recorder.waits) >= 2


def test_other_403_raises(make_client):
    client, _, _ = make_client(replies(error_response(403, "forbidden", {"reason": "suspended"})))
    with pytest.raises(AgentLandError) as info:
        next(iter(client.events()))
    assert info.value.status == 403
