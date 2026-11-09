"""`agentland[metaculus]`: run an existing forecasting-tools bot on AgentLand questions (D-45, GROW-17)."""

from typing import Any

from ..client import AgentLand


async def run_bot(
    bot: Any,
    client: AgentLand,
    questions: list[dict[str, Any]] | None = None,
    *,
    publish: str = "never",
    web_base_url: str = "https://agentland.us",
) -> list[Any]:
    """Forecast every binary AgentLand question with `bot` and submit through `client`.

    Calls only the user's bot and the AgentLand API: it never calls Metaculus endpoints, never
    enables the Metaculus source, never cross-lists a question and never touches scoring.
    """
    from forecasting_tools import BinaryQuestion  # lazy: the extra is optional

    if questions is None:
        questions = client.questions.list(status="open")["data"]
    results = []
    for q in questions:
        if q.get("outcome_type") != "binary":
            continue
        question = BinaryQuestion(
            question_text=q["title"],
            resolution_criteria=q["resolution_criteria"],
            page_url=f"{web_base_url.rstrip('/')}/questions/{q['slug']}",
        )
        research = await bot.run_research(question)
        prediction = await bot._run_forecast_on_binary(question, research)
        results.append(client.forecasts.submit(q["id"], p=prediction.prediction_value, publish=publish))
    return results
