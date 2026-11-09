import json
import sys
import types
from dataclasses import dataclass
from typing import Callable

import httpx
import pytest

BASE_URL = "https://api.test"
API_KEY = "al_test"


class Recorder:
    """Injected `sleep`: records waits instead of sleeping."""

    def __init__(self) -> None:
        self.waits: list[float] = []

    def __call__(self, seconds: float) -> None:
        self.waits.append(seconds)


def json_response(status: int, body: object, headers: dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(
        status,
        content=json.dumps(body).encode(),
        headers={"content-type": "application/json", **(headers or {})},
    )


def error_response(status: int, code: str, details: object = None, headers: dict[str, str] | None = None) -> httpx.Response:
    return json_response(
        status,
        {"error": {"code": code, "message": code, "details": details, "request_id": "req_1"}},
        headers,
    )


@pytest.fixture
def make_client():
    """`make_client(handler, **kw)` -> (client, requests, recorder)."""

    def build(handler: Callable[[httpx.Request], httpx.Response], **kwargs):
        from agentland import AgentLand

        requests: list[httpx.Request] = []

        def recording(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return handler(request)

        recorder = Recorder()
        client = AgentLand(
            api_key=API_KEY,
            base_url=BASE_URL,
            transport=httpx.MockTransport(recording),
            sleep=recorder,
            **kwargs,
        )
        return client, requests, recorder

    return build


@dataclass
class FakeBinaryQuestion:
    question_text: str
    resolution_criteria: str
    page_url: str


@pytest.fixture
def fake_forecasting_tools(monkeypatch):
    """A stand-in `forecasting_tools` module: no real model, no Metaculus token."""
    module = types.ModuleType("forecasting_tools")
    module.BinaryQuestion = FakeBinaryQuestion
    monkeypatch.setitem(sys.modules, "forecasting_tools", module)
    return module
