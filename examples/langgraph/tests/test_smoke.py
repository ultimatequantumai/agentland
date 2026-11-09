"""Smoke test: the starter lists questions and submits one forecast through MCP with a scripted fake model."""

import asyncio
import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Static imports: a missing starter fails even when the stack env is absent.
from bot import run, with_idempotency_key  # noqa: E402
from fake_model import ScriptedChatModel  # noqa: E402

REQUIRED = (
    "AGENTLAND_API_KEY",
    "AGENTLAND_MCP_URL",
    "AGENTLAND_QUESTION_ID",
    "AGENTLAND_EXAMPLES_CONTROL_URL",
)
_missing = [name for name in REQUIRED if not os.environ.get(name)]
if _missing:
    if os.environ.get("AGENTLAND_EXAMPLES_REQUIRED") == "1":
        raise RuntimeError(f"AGENTLAND_EXAMPLES_REQUIRED=1 but missing: {', '.join(_missing)}")
    pytest.skip(f"examples stack env absent: {', '.join(_missing)}", allow_module_level=True)


def control_forecasts() -> dict:
    url = f"{os.environ['AGENTLAND_EXAMPLES_CONTROL_URL']}/__examples/forecasts"
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.load(response)


def stack_question_ids() -> set:
    return {os.environ["AGENTLAND_QUESTION_ID"], os.environ.get("AGENTLAND_QUESTION_ID_2", "")} - {""}


def as_body(result):
    """Tool results arrive as a dict, JSON text, or MCP content blocks depending on the framework."""
    if isinstance(result, dict):
        return result.get("structuredContent", result)
    if isinstance(result, (list, tuple)):
        for block in result:
            text = block.get("text") if isinstance(block, dict) else getattr(block, "text", None)
            if text:
                return as_body(text)
        return {}
    if isinstance(result, str):
        try:
            return as_body(json.loads(result))
        except ValueError:
            return {}
    return as_body(getattr(result, "content", {}))


def test_fake_model_lists_questions_and_submits_one_forecast():
    assert not os.environ.get("OPENAI_API_KEY"), "the smoke test must not see a model-provider key"
    before = control_forecasts()

    trace = asyncio.run(run(model=ScriptedChatModel()))

    tools = [step["tool"] for step in trace]
    assert "list_questions" in tools and "submit_forecast" in tools
    assert tools.index("list_questions") < tools.index("submit_forecast")
    submits = [step for step in trace if step["tool"] == "submit_forecast"]
    assert len(submits) == 1
    submit = submits[0]
    assert submit["args"]["question_id"] in stack_question_ids()
    uuid.UUID(submit["args"]["idempotency_key"])
    assert as_body(submit["result"]).get("id")

    after = control_forecasts()
    assert after["count"] == before["count"] + 1
    assert after["latest"]["question_id"] in stack_question_ids()
    assert after["latest"]["idempotency_key_present"] is True


def test_with_idempotency_key_is_fresh_per_call_and_replaces_model_value():
    args = {"question_id": os.environ["AGENTLAND_QUESTION_ID"], "p": 0.5, "idempotency_key": "model-said-this"}
    first = with_idempotency_key(args)
    second = with_idempotency_key(args)
    assert first["idempotency_key"] != second["idempotency_key"]
    for out in (first, second):
        assert out["idempotency_key"] != "model-said-this"
        uuid.UUID(out["idempotency_key"])
        assert out["question_id"] == args["question_id"]
    assert args["idempotency_key"] == "model-said-this"
