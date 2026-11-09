import asyncio
import importlib
import json
import sys
from types import SimpleNamespace

from conftest import BASE_URL, json_response

BINARY = {
    "id": "00000000-0000-4000-8000-000000000001",
    "slug": "will-it-rain-2026-11-01",
    "title": "Will it rain in Paris on 2026-11-01?",
    "resolution_criteria": "Resolves YES if Météo-France reports ≥ 0.1 mm.",
    "outcome_type": "binary",
}
NON_BINARY = {
    "id": "00000000-0000-4000-8000-000000000009",
    "slug": "paris-rainfall-mm",
    "title": "How much rain?",
    "resolution_criteria": "mm reported.",
    "outcome_type": "numeric",
}


class StubBot:
    def __init__(self):
        self.questions = []

    async def run_research(self, question):
        return "research"

    async def _run_forecast_on_binary(self, question, research):
        self.questions.append(question)
        return SimpleNamespace(prediction_value=0.62, reasoning="stub")


def run(make_client, **kwargs):
    from agentland.adapters.metaculus import run_bot

    client, requests, _ = make_client(lambda r: json_response(201, {"id": "f1", "p": 0.62}))
    bot = StubBot()
    asyncio.run(run_bot(bot, client, questions=[BINARY, NON_BINARY], **kwargs))
    return bot, requests


def test_stub_bot_forecast_submitted_via_sdk_with_idempotency_key(make_client, fake_forecasting_tools):
    bot, requests = run(make_client)
    assert len(requests) == 1
    (request,) = requests
    assert request.method == "POST"
    assert request.url.path == f"/v1/questions/{BINARY['id']}/forecasts"
    assert json.loads(request.content)["p"] == 0.62
    assert request.headers.get("Idempotency-Key")
    assert all(f"{r.url.scheme}://{r.url.host}" == BASE_URL for r in requests)

    (question,) = bot.questions
    assert isinstance(question, fake_forecasting_tools.BinaryQuestion)
    assert question.question_text == BINARY["title"]
    assert question.resolution_criteria == BINARY["resolution_criteria"]
    assert question.page_url == f"https://agentland.us/questions/{BINARY['slug']}"
    assert "/q/" not in question.page_url


def test_web_base_url_override(make_client, fake_forecasting_tools):
    bot, _ = run(make_client, web_base_url="https://staging.example")
    assert bot.questions[0].page_url == f"https://staging.example/questions/{BINARY['slug']}"


def test_import_without_forecasting_tools(monkeypatch):
    monkeypatch.setitem(sys.modules, "forecasting_tools", None)  # any import of it now fails
    for name in [m for m in sys.modules if m == "agentland" or m.startswith("agentland.")]:
        monkeypatch.delitem(sys.modules, name)
    importlib.import_module("agentland")
    importlib.import_module("agentland.adapters.metaculus")
