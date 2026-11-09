"""Scripted CrewAI LLM for CI: ReAct text, no network, no provider key."""

import json
import re

from crewai.llms.base_llm import BaseLLM

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def _text(messages) -> str:
    if isinstance(messages, str):
        return messages
    return "\n".join(str(m.get("content", "")) if isinstance(m, dict) else str(m) for m in messages)


def _tool_name(text: str, suffix: str) -> str:
    """The tool's name as CrewAI listed it (it may carry a server prefix)."""
    match = re.search(rf"Tool Name: ([\w.-]*{suffix})", text)
    return match.group(1) if match else suffix


def first_question_id(observation: str) -> str:
    """The first question's id from the list_questions observation, JSON first, else the text."""
    start = observation.find("{")
    if start != -1:
        try:
            body, _ = json.JSONDecoder().raw_decode(observation[start:])
            return body["data"][0]["id"]
        except (ValueError, KeyError, IndexError, TypeError):
            pass
    return UUID.search(observation).group(0)


class ScriptedLLM(BaseLLM):
    """list_questions, then submit_forecast on the first listed question, then Final Answer."""

    def __init__(self):
        super().__init__(model="scripted-fake")

    def supports_function_calling(self) -> bool:
        return False

    def supports_stop_words(self) -> bool:
        return False

    def get_context_window_size(self) -> int:
        return 32_000

    def call(self, messages, *args, **kwargs) -> str:
        # A step counter, not the prompt: CrewAI's ReAct template itself mentions "Observation:".
        step = getattr(self, "_scripted_step", 0)
        object.__setattr__(self, "_scripted_step", step + 1)
        text = _text(messages)
        if step == 0:
            name = _tool_name(text, "list_questions")
            return f"Thought: list open questions\nAction: {name}\nAction Input: {{}}"
        if step == 1:
            submit = {
                "question_id": first_question_id(text.split("Observation:")[-1]),
                "p": 0.5,
                "rationale": "starter fake: no view, even odds",
            }
            name = _tool_name(text, "submit_forecast")
            return f"Thought: submit one forecast\nAction: {name}\nAction Input: {json.dumps(submit)}"
        return "Thought: submitted\nFinal Answer: done"
