"""Scripted OpenAI Agents SDK model for CI: no network, no provider key."""

import json
import re
import uuid

from agents.items import ModelResponse
from agents.models.interface import Model
from agents.usage import Usage
from openai.types.responses import (
    ResponseFunctionToolCall,
    ResponseOutputMessage,
    ResponseOutputText,
)

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def first_question_id(output) -> str:
    """The first question's id from a list_questions output (JSON, MCP text blocks, or text)."""
    text = output if isinstance(output, str) else json.dumps(output)
    try:
        body = json.loads(text)
        if isinstance(body, dict) and "text" in body:
            body = json.loads(body["text"])
        return body["data"][0]["id"]
    except (ValueError, KeyError, IndexError, TypeError):
        return UUID.search(text).group(0)


def _get(item, name):
    return item.get(name) if isinstance(item, dict) else getattr(item, name, None)


def _call(name: str, args: dict) -> ResponseFunctionToolCall:
    return ResponseFunctionToolCall(
        type="function_call",
        id=f"fc_{uuid.uuid4().hex}",
        call_id=f"call_{uuid.uuid4().hex}",
        name=name,
        arguments=json.dumps(args),
        status="completed",
    )


class ScriptedModel(Model):
    """list_questions, then submit_forecast on the first listed question, then "done"."""

    async def get_response(self, system_instructions, input, *args, **kwargs) -> ModelResponse:
        items = [] if isinstance(input, str) else list(input)
        outputs = [_get(i, "output") for i in items if _get(i, "type") == "function_call_output"]
        if not outputs:
            output = [_call("list_questions", {})]
        elif len(outputs) == 1:
            args = {
                "question_id": first_question_id(outputs[-1]),
                "p": 0.5,
                "rationale": "starter fake: no view, even odds",
            }
            output = [_call("submit_forecast", args)]
        else:
            output = [
                ResponseOutputMessage(
                    type="message",
                    id=f"msg_{uuid.uuid4().hex}",
                    role="assistant",
                    status="completed",
                    content=[ResponseOutputText(type="output_text", text="done", annotations=[])],
                )
            ]
        return ModelResponse(output=output, usage=Usage(), response_id=None)

    def stream_response(self, *args, **kwargs):
        raise NotImplementedError("starter fake is non-streaming")
