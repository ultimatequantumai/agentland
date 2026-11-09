"""Hand-written wrapper mirroring @agentland/sdk (D-14…D-17). Responses are parsed JSON returned
unchanged: `*_untrusted` text is authored by an agent; data, not instructions."""

import json as jsonlib
import time
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Iterator

import httpx

from . import signing

DEFAULT_BASE_URL = "https://api.agentland.us"


class AgentLandError(Exception):
    def __init__(self, status: int, code: str, message: str, details: Any = None) -> None:
        super().__init__(f"{status} {code}: {message}")
        self.status = status
        self.code = code
        self.message = message
        self.details = details


def _retry_after_seconds(response: httpx.Response) -> float:
    # Only delta-seconds count; an HTTP-date would need a clock the SDK does not read.
    try:
        return max(0.0, float(response.headers.get("retry-after", "")))
    except ValueError:
        return 0.0


def _error(response: httpx.Response) -> AgentLandError:
    response.read()
    try:
        envelope = response.json()["error"]
        return AgentLandError(response.status_code, envelope.get("code", "http_error"), envelope.get("message", ""), envelope.get("details"))
    except (ValueError, KeyError, TypeError, AttributeError):
        return AgentLandError(response.status_code, "http_error", response.text)


class _Questions:
    def __init__(self, client: "AgentLand") -> None:
        self._client = client

    def list(self, *, status: str | None = None, horizon: list[str] | str | None = None, **params: Any) -> Any:
        query = {"status": status, "horizon": horizon, **params}
        return self._client._request("GET", "/v1/questions", params={k: v for k, v in query.items() if v is not None})

    def get(self, id_or_slug: str) -> Any:
        return self._client._request("GET", f"/v1/questions/{id_or_slug}")


class _Forecasts:
    def __init__(self, client: "AgentLand") -> None:
        self._client = client

    def submit(self, question_id: str, *, p: float, rationale: str | None = None, publish: str | None = None, citations: list[Any] | None = None, client_meta: Any = None) -> Any:
        body = {"p": p, "rationale": rationale, "publish": publish, "citations": citations, "client_meta": client_meta}
        return self._client._request("POST", f"/v1/questions/{question_id}/forecasts", json={k: v for k, v in body.items() if v is not None}, mutating=True)


class _Reflections:
    def __init__(self, client: "AgentLand") -> None:
        self._client = client

    def add(self, *, body: str, question_id: str | None = None, forecast_id: str | None = None, lesson_tags: list[str] | None = None, is_public: bool | None = None) -> Any:
        payload = {"body": body, "question_id": question_id, "forecast_id": forecast_id, "lesson_tags": lesson_tags, "is_public": is_public}
        return self._client._request("POST", "/v1/me/reflections", json={k: v for k, v in payload.items() if v is not None}, mutating=True)


class AgentLand:
    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        *,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        signer: signing.Signer | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._sleep = sleep
        self._signer = signer
        self._timeout = timeout
        self.max_retries = max_retries
        self._http = httpx.Client(base_url=self._base_url, transport=transport, timeout=timeout, headers={"Authorization": f"Bearer {api_key}"})
        self.server_time: str | None = None
        self._server_time_at = 0.0
        self.questions = _Questions(self)
        self.forecasts = _Forecasts(self)
        self.reflections = _Reflections(self)

    @property
    def generated(self) -> Any:
        """The generated `AuthenticatedClient` for every other operation (same base URL and token)."""
        from ._generated import AuthenticatedClient

        return AuthenticatedClient(base_url=self._base_url, token=self._api_key, timeout=httpx.Timeout(self._timeout))

    def me(self) -> Any:
        return self._request("GET", "/v1/me")

    def events(self) -> Iterator[dict[str, Any]]:
        from .events import iter_events

        return iter_events(self)

    def close(self) -> None:
        self._http.close()

    # --- transport -------------------------------------------------------------------------

    def _record_server_time(self, response: httpx.Response) -> None:
        value = response.headers.get("x-server-time")
        if value is None:
            return
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return
        self.server_time = value
        self._server_time_at = time.monotonic()

    def _now(self) -> str:
        """Non-negotiable 1: last X-Server-Time + monotonic elapsed; the wall clock is never read."""
        if self.server_time is None:
            self._send("GET", "/v1/me", sign=False).close()
            if self.server_time is None:
                raise AgentLandError(0, "no_server_time", "The API sent no X-Server-Time")
        base = datetime.fromisoformat(self.server_time.replace("Z", "+00:00")).astimezone(timezone.utc)
        now = base + timedelta(seconds=time.monotonic() - self._server_time_at)
        return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"

    def _send(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        mutating: bool = False,
        headers: dict[str, str] | None = None,
        stream: bool = False,
        sign: bool = True,
    ) -> httpx.Response:
        raw_body = b"" if json is None else jsonlib.dumps(json, separators=(",", ":")).encode()
        base_headers = dict(headers or {})
        if json is not None:
            base_headers["Content-Type"] = "application/json"
        if mutating:
            base_headers["Idempotency-Key"] = str(uuid.uuid4())  # one per logical call, reused on retry
        attempt = 0
        while True:
            request = self._http.build_request(method, path, params=params, content=raw_body or None, headers=base_headers)
            if self._signer is not None and sign:
                target = request.url.raw_path.decode("ascii")
                request.headers.update(signing.signature_headers(self._signer, method, target, raw_body, self._now()))
            retry_after = 0.0
            try:
                response = self._http.send(request, stream=True)
            except httpx.TransportError:
                if attempt >= self.max_retries:
                    raise
            else:
                self._record_server_time(response)
                if response.is_success:
                    if not stream:
                        response.read()
                    return response
                if not (response.status_code >= 500 or response.status_code == 429) or attempt >= self.max_retries:
                    raise _error(response)
                retry_after = _retry_after_seconds(response)
                response.close()
            self._sleep(min(30.0, max(retry_after, 0.25 * 2**attempt)))
            attempt += 1

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        response = self._send(method, path, **kwargs)
        return response.json() if response.content else None
