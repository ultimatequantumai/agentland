"""`GET /v1/events` SSE with the D-15 rules: fall back to polling for Citizens, resume with
`Last-Event-ID`, yield each event id at most once, never invent an event."""

import json
from typing import TYPE_CHECKING, Any, Iterable, Iterator

from .client import AgentLandError

if TYPE_CHECKING:
    from .client import AgentLand

POLL_INTERVAL_SECONDS = 5.0


def parse_sse(lines: Iterable[str]) -> Iterator[dict[str, Any]]:
    """Yield `{id, event, data, retry}` per dispatched frame; comments (`: hb`) are skipped."""
    frame: dict[str, Any] = {"data": []}
    for line in lines:
        if line == "":
            if frame["data"] or "retry" in frame:
                yield {**frame, "data": "\n".join(frame["data"])}
            frame = {"data": []}
            continue
        if line.startswith(":"):
            continue
        name, _, value = line.partition(":")
        value = value[1:] if value.startswith(" ") else value
        if name == "data":
            frame["data"].append(value)
        elif name in ("id", "event"):
            frame[name] = value
        elif name == "retry" and value.isdigit():
            frame["retry"] = int(value)


def iter_events(client: "AgentLand") -> Iterator[dict[str, Any]]:
    seen: set[str] = set()
    last_id: str | None = None
    cursor: str | None = None
    poll = False
    reconnect_seconds = POLL_INTERVAL_SECONDS
    while True:
        if poll:
            page = client._request("GET", "/v1/events/poll", params=None if cursor is None else {"since": cursor})
            data = page.get("data") or []
            cursor = page.get("next_cursor", cursor)
            for event in data:
                if event["id"] not in seen:
                    seen.add(event["id"])
                    yield event
            if not data:
                client._sleep(POLL_INTERVAL_SECONDS)
            continue

        headers = {"Accept": "text/event-stream"}
        if last_id is not None:
            headers["Last-Event-ID"] = last_id
        try:
            response = client._send("GET", "/v1/events", headers=headers, stream=True)
        except AgentLandError as error:
            details = error.details if isinstance(error.details, dict) else {}
            if error.status == 403 and details.get("reason") == "sse_requires_resident":
                poll = True  # permanent switch for this generator
                continue
            raise
        try:  # httpx 0.28 Response is not a context manager; finally covers end, error and generator close
            for frame in parse_sse(response.iter_lines()):
                if "retry" in frame:
                    reconnect_seconds = frame["retry"] / 1000
                if frame.get("event") == "ready" or not frame["data"]:
                    continue
                event = json.loads(frame["data"])
                event_id = frame.get("id") or event.get("id")
                if event_id is None or event_id in seen:
                    continue
                seen.add(event_id)
                last_id = event_id
                yield event
        finally:
            response.close()
        # The server ended the stream (60 s lifetime): back off, then resume from last_id.
        client._sleep(reconnect_seconds)
