"""Scripted chat model for CI: no network, no provider key."""

import json
import uuid

from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult


def first_question_id(content) -> str:
    """The first question's id from a list_questions result (JSON text or MCP content blocks)."""
    if isinstance(content, list):
        content = "".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content)
    return json.loads(content)["data"][0]["id"]


class ScriptedChatModel(GenericFakeChatModel):
    """list_questions, then submit_forecast on the first listed question, then "done"."""

    messages: object = iter(())

    def bind_tools(self, tools, **kwargs):
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        results = [m for m in messages if isinstance(m, ToolMessage)]
        if not results:
            reply = AIMessage(content="", tool_calls=[_call("list_questions", {})])
        elif len(results) == 1:
            args = {
                "question_id": first_question_id(results[-1].content),
                "p": 0.5,
                "rationale": "starter fake: no view, even odds",
            }
            reply = AIMessage(content="", tool_calls=[_call("submit_forecast", args)])
        else:
            reply = AIMessage(content="done")
        return ChatResult(generations=[ChatGeneration(message=reply)])


def _call(name: str, args: dict) -> dict:
    return {"name": name, "args": args, "id": f"call_{uuid.uuid4().hex}", "type": "tool_call"}
