from __future__ import annotations

from datetime import datetime, timezone

import pytest

from requests_oauth2client.utils import accepts_expires_in, validate_endpoint_uri


def test_validate_uri() -> None:
    validate_endpoint_uri("https://myas.local/token")
    with pytest.raises(ValueError, match="https"):
        validate_endpoint_uri("http://myas.local/token")
    with pytest.raises(ValueError, match="path"):
        validate_endpoint_uri("https://myas.local")
    with pytest.raises(ValueError, match="fragment"):
        validate_endpoint_uri("https://myas.local/token#foo")
    with pytest.raises(ValueError, match="username"):
        validate_endpoint_uri("https://user:passwd@myas.local/token")
    with pytest.raises(ValueError, match="port"):
        validate_endpoint_uri("https://myas.local:1234/token")


@pytest.mark.parametrize("expires_in", [10, "10"])
def test_accepts_expires_in(expires_in: int | str) -> None:
    @accepts_expires_in
    def foo(expires_at: datetime | None = None) -> datetime | None:
        return expires_at

    now = datetime.now(tz=timezone.utc)
    assert foo(expires_at=now) == now
    assert foo(now) == now
    assert isinstance(foo(expires_in=expires_in), datetime)
    assert foo() is None
