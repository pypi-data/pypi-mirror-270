"""This module contains classes that represent Tokens used in OAuth2.0 / OIDC."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import TYPE_CHECKING, Any, Callable, ClassVar

import jwskate
from attrs import Factory, asdict, frozen
from binapy import BinaPy
from typing_extensions import Self

from .exceptions import (
    ExpiredIdToken,
    InvalidIdToken,
    MismatchingAcr,
    MismatchingAudience,
    MismatchingAzp,
    MismatchingIdTokenAlg,
    MismatchingIssuer,
    MismatchingNonce,
    MissingIdToken,
)
from .utils import accepts_expires_in

if TYPE_CHECKING:
    from .authorization_request import AuthorizationResponse
    from .client import OAuth2Client


class TokenType(str, Enum):
    """An enum of standardised `token_type` values."""

    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"
    ID_TOKEN = "id_token"


class AccessTokenType(str, Enum):
    """An enum of standardised `access_token` types."""

    BEARER = "Bearer"


class IdToken(jwskate.SignedJwt):
    """Represent an ID Token.

    An ID Token is actually a Signed JWT. If the ID Token is encrypted, it must be decoded
    beforehand.

    """

    @property
    def auth_time(self) -> datetime:
        """The last user authentication time."""
        auth_time = self.claims.get("auth_time")
        if auth_time:
            return self.timestamp_to_datetime(auth_time)
        msg = "This ID Token doesn't have an `auth_time` attribute."
        raise AttributeError(msg)

    @classmethod
    def hash_method(cls, key: jwskate.Jwk, alg: str | None = None) -> Callable[[str], str]:
        """Returns a callable that generates valid OIDC hashes, such as at_hash, c_hash, s_hash.

        Args:
            key: the ID token signature verification public key
            alg: the ID token signature algorithm

        Returns:
            a callable that takes a string as input and produces a valid hash as a str output

        """
        alg_class = jwskate.select_alg_class(key.SIGNATURE_ALGORITHMS, jwk_alg=key.alg, alg=alg)
        if alg_class == jwskate.EdDsa:
            if key.crv == "Ed25519":

                def hash_method(token: str) -> str:
                    return BinaPy(token).to("sha512")[:32].to("b64u").decode()

            elif key.crv == "Ed448":

                def hash_method(token: str) -> str:
                    return BinaPy(token).to("shake256", 456).to("b64u").decode()

        else:
            hash_alg = alg_class.hashing_alg.name
            hash_size = alg_class.hashing_alg.digest_size

            def hash_method(token: str) -> str:
                return BinaPy(token).to(hash_alg)[: hash_size // 2].to("b64u").decode()

        return hash_method


class AccessToken:
    """Base class for Access Tokens."""

    TOKEN_TYPE: ClassVar[str]


@frozen(init=False)
class BearerToken(AccessToken):
    """Represents a Bearer Token as returned by a Token Endpoint.

    This is a wrapper around a Bearer Token and associated parameters, such as expiration date and
    refresh token, as returned by an OAuth 2.x or OIDC 1.0 Token Endpoint.

    All parameters are as returned by a Token Endpoint. The token expiration date can be passed as
    datetime in the `expires_at` parameter, or an `expires_in` parameter, as number of seconds in
    the future, can be passed instead.

    Args:
        access_token: an `access_token`, as returned by the AS.
        expires_at: an expiration date. This method also accepts an `expires_in` hint as
            returned by the AS, if any.
        scope: a `scope`, as returned by the AS, if any.
        refresh_token: a `refresh_token`, as returned by the AS, if any.
        token_type: a `token_type`, as returned by the AS.
        id_token: an `id_token`, as returned by the AS, if any.
        **kwargs: additional parameters as returned by the AS, if any.

    """

    TOKEN_TYPE: ClassVar[str] = AccessTokenType.BEARER.value

    access_token: str
    expires_at: datetime | None = None
    scope: str | None = None
    refresh_token: str | None = None
    token_type: str = TOKEN_TYPE
    id_token: IdToken | jwskate.JweCompact | None = None
    kwargs: dict[str, Any] = Factory(dict)

    @accepts_expires_in
    def __init__(
        self,
        access_token: str,
        *,
        expires_at: datetime | None = None,
        scope: str | None = None,
        refresh_token: str | None = None,
        token_type: str = TOKEN_TYPE,
        id_token: str | bytes | IdToken | jwskate.JweCompact | None = None,
        **kwargs: Any,
    ):
        if token_type.title() != self.TOKEN_TYPE.title():
            msg = f"Token Type is not '{self.TOKEN_TYPE}'!"
            raise ValueError(msg, token_type)
        id_token_jwt: IdToken | jwskate.JweCompact | None = None
        if isinstance(id_token, (str, bytes)):
            try:
                id_token_jwt = IdToken(id_token)
            except jwskate.InvalidJwt:
                try:
                    id_token_jwt = jwskate.JweCompact(id_token)
                except jwskate.InvalidJwe:
                    msg = "ID Token is invalid because it is  neither a JWT or a JWE."
                    raise InvalidIdToken(msg) from None
        else:
            id_token_jwt = id_token
        self.__attrs_init__(
            access_token=access_token,
            expires_at=expires_at,
            scope=scope,
            refresh_token=refresh_token,
            token_type=token_type,
            id_token=id_token_jwt,
            kwargs=kwargs,
        )

    def is_expired(self, leeway: int = 0) -> bool | None:
        """Check if the access token is expired.

        Args:
            leeway: If the token expires in the next given number of seconds,
                then consider it expired already.

        Returns:
            One of:

            - `True` if the access token is expired
            - `False` if it is still valid
            - `None` if there is no expires_in hint.

        """
        if self.expires_at:
            return datetime.now(tz=timezone.utc) + timedelta(seconds=leeway) > self.expires_at
        return None

    def authorization_header(self) -> str:
        """Return the appropriate Authorization Header value for this token.

        The value is formatted correctly according to RFC6750.

        Returns:
            the value to use in an HTTP Authorization Header

        """
        return f"Bearer {self.access_token}"

    def validate_id_token(self, client: OAuth2Client, azr: AuthorizationResponse) -> Self:  # noqa: C901, PLR0915
        """Validate that a token response is valid, and return the ID Token.

        This will validate the id_token as described in [OIDC 1.0
        $3.1.3.7](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).

        If the ID Token is encrypted, this decrypts it and returns the clear-text ID Token.

        """
        if not self.id_token:
            raise MissingIdToken()

        raw_id_token = self.id_token

        if isinstance(raw_id_token, jwskate.JweCompact) and client.id_token_encrypted_response_alg is None:
            msg = "ID Token is encrypted while it should be clear-text"
            raise InvalidIdToken(msg, self)
        elif isinstance(raw_id_token, IdToken) and client.id_token_encrypted_response_alg is not None:
            msg = "ID Token is clear-text while it should be encrypted"
            raise InvalidIdToken(msg, self)

        if isinstance(raw_id_token, jwskate.JweCompact):
            enc_jwk = client.id_token_decryption_key
            if enc_jwk is None:
                msg = "ID Token is encrypted but client does not have a decryption key"
                raise InvalidIdToken(msg, self)
            nested_id_token = raw_id_token.decrypt(enc_jwk)
            id_token = IdToken(nested_id_token)
        else:
            id_token = raw_id_token

        if id_token.get_header("alg") is None and client.id_token_signed_response_alg is None:
            msg = (
                "ID Token does not contain an `alg` parameter to specify the signature"
                " algorithm, and no algorithm has been configured for the client (using param"
                " id_token_signed_response_alg`."
            )
            raise InvalidIdToken(msg)
        elif client.id_token_signed_response_alg is not None and id_token.alg != client.id_token_signed_response_alg:
            raise MismatchingIdTokenAlg(id_token.alg, client.id_token_signed_response_alg)

        id_token_alg = id_token.alg or client.id_token_signed_response_alg

        if azr.issuer and id_token.issuer != azr.issuer:
            raise MismatchingIssuer(id_token.issuer, azr.issuer, self)

        if id_token.audiences and client.client_id not in id_token.audiences:
            raise MismatchingAudience(id_token.audiences, client.client_id, self)

        if id_token.get_claim("azp") is not None and id_token.azp != client.client_id:
            raise MismatchingAzp(id_token.azp, client.client_id, self)

        if id_token.is_expired():
            raise ExpiredIdToken(id_token)

        if azr.nonce and id_token.nonce != azr.nonce:
            raise MismatchingNonce()

        if azr.acr_values and id_token.acr not in azr.acr_values:
            raise MismatchingAcr(id_token.acr, azr.acr_values)

        hash_function: Callable[[str], str]  # method used to calculate at_hash, s_hash, etc.

        if id_token_alg in jwskate.SignatureAlgs.ALL_SYMMETRIC:
            if not client.client_secret:
                msg = "ID Token is symmetrically signed but this client does not have a Client Secret."
                raise InvalidIdToken(msg)
            id_token.verify_signature(jwskate.SymmetricJwk.from_bytes(client.client_secret), alg=id_token_alg)
        elif id_token_alg in jwskate.SignatureAlgs.ALL_ASYMMETRIC:
            if not client.authorization_server_jwks:
                msg = "ID Token is asymmetrically signed but the Authorization Server JWKS is not available."
                raise InvalidIdToken(msg)

            if id_token.get_header("kid") is None:
                msg = (
                    "ID Token does not contain a Key ID (kid) to specify the asymmetric key "
                    "to use for signature verification."
                )
                raise InvalidIdToken(msg)
            try:
                verification_jwk = client.authorization_server_jwks.get_jwk_by_kid(id_token.kid)
            except KeyError:
                msg = (
                    f"ID Token is asymmetrically signed but its Key ID '{id_token.kid}' "
                    "is not part of the Authorization Server JWKS."
                )
                raise InvalidIdToken(msg) from None

            if id_token_alg not in verification_jwk.supported_signing_algorithms():
                msg = "ID Token is asymmetrically signed but its algorithm is not supported by the verification key."
                raise InvalidIdToken(msg)

            id_token.verify_signature(verification_jwk, alg=id_token_alg)

            hash_function = IdToken.hash_method(verification_jwk, id_token_alg)

        at_hash = id_token.get_claim("at_hash")
        if at_hash is not None:
            expected_at_hash = hash_function(self.access_token)
            if expected_at_hash != at_hash:
                msg = f"Mismatching 'at_hash' value: expected '{expected_at_hash}', got '{at_hash}'"
                raise InvalidIdToken(msg)

        c_hash = id_token.get_claim("c_hash")
        if c_hash is not None:
            expected_c_hash = hash_function(azr.code)
            if expected_c_hash != c_hash:
                msg = f"Mismatching 'c_hash' value: expected '{expected_c_hash}', got '{c_hash}'"
                raise InvalidIdToken(msg)

        s_hash = id_token.get_claim("s_hash")
        if s_hash is not None:
            if azr.state is None:
                msg = "ID Token has a 's_hash' claim but no state was included in the request."
                raise InvalidIdToken(msg)
            expected_s_hash = hash_function(azr.state)
            if expected_s_hash != s_hash:
                msg = f"Mismatching 's_hash' value (expected '{expected_s_hash}', got '{s_hash}'"
                raise InvalidIdToken(msg)

        if azr.max_age is not None:
            try:
                auth_time = id_token.auth_time
            except AttributeError:
                msg = (
                    "A `max_age` parameter was included in the authorization request, "
                    "but the ID Token does not contain an `auth_time` claim."
                )
                raise InvalidIdToken(msg) from None
            auth_age = datetime.now(tz=timezone.utc) - auth_time
            if auth_age.seconds > azr.max_age + 60:
                msg = (
                    "User authentication happened too long ago. The `auth_time` parameter from"
                    " the ID Token indicate that the last Authentication Time was at"
                    f" {auth_time} ({auth_age.seconds} sec ago), but the authorization request"
                    f" `max_age` parameter specified that it must be maximum {azr.max_age} sec"
                    " ago."
                )
                raise InvalidIdToken(msg)

        return self.__class__(
            access_token=self.access_token,
            expires_at=self.expires_at,
            scope=self.scope,
            refresh_token=self.refresh_token,
            token_type=self.token_type,
            id_token=id_token,
            **self.kwargs,
        )

    def __str__(self) -> str:
        """Return the access token value, as a string.

        Returns:
            the access token string

        """
        return self.access_token

    def as_dict(self) -> dict[str, Any]:
        """Return a dict of parameters.

        That is suitable for serialization or to init another BearerToken.

        """
        d = asdict(self)
        d.pop("expires_at")
        d["expires_in"] = self.expires_in
        d.update(**d.pop("kwargs", {}))
        return {key: val for key, val in d.items() if val is not None}

    @property
    def expires_in(self) -> int | None:
        """Number of seconds until expiration."""
        if self.expires_at:
            return int(self.expires_at.timestamp() - datetime.now(tz=timezone.utc).timestamp())
        return None

    def __getattr__(self, key: str) -> Any:
        """Return custom attributes from this BearerToken.

        Args:
            key: a key

        Returns:
            the associated value in this token response

        Raises:
            AttributeError: if the attribute is not found in this response.

        """
        return self.kwargs.get(key) or super().__getattribute__(key)


class BearerTokenSerializer:
    """A helper class to serialize Token Response returned by an AS.

    This may be used to store BearerTokens in session or cookies.

    It needs a `dumper` and a `loader` functions that will respectively serialize and deserialize
    BearerTokens. Default implementations are provided with use gzip and base64url on the serialized
    JSON representation.

    Args:
        dumper: a function to serialize a token into a `str`.
        loader: a function to deserialize a serialized token representation.

    """

    def __init__(
        self,
        dumper: Callable[[BearerToken], str] | None = None,
        loader: Callable[[str], BearerToken] | None = None,
    ):
        self.dumper = dumper or self.default_dumper
        self.loader = loader or self.default_loader

    @staticmethod
    def default_dumper(token: BearerToken) -> str:
        """Serialize a token as JSON, then compress with deflate, then encodes as base64url.

        Args:
            token: the `BearerToken` to serialize

        Returns:
            the serialized value

        """
        return BinaPy.serialize_to("json", token.as_dict()).to("deflate").to("b64u").ascii()

    def default_loader(self, serialized: str, token_class: type[BearerToken] = BearerToken) -> BearerToken:
        """Deserialize a BearerToken.

        This does the opposite operations than `default_dumper`.

        Args:
            serialized: the serialized token
            token_class: class to use to deserialize the Token

        Returns:
            a BearerToken

        """
        attrs = BinaPy(serialized).decode_from("b64u").decode_from("deflate").parse_from("json")
        expires_at = attrs.get("expires_at")
        if expires_at:
            attrs["expires_at"] = datetime.fromtimestamp(expires_at, tz=timezone.utc)
        return token_class(**attrs)

    def dumps(self, token: BearerToken) -> str:
        """Serialize and compress a given token for easier storage.

        Args:
            token: a BearerToken to serialize

        Returns:
            the serialized token, as a str

        """
        return self.dumper(token)

    def loads(self, serialized: str) -> BearerToken:
        """Deserialize a serialized token.

        Args:
            serialized: the serialized token

        Returns:
            the deserialized token

        """
        return self.loader(serialized)


class DPoPToken(AccessToken):
    """Represents a DPoP Token."""
