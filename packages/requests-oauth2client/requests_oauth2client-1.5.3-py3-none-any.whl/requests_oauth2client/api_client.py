"""`ApiClient` main module."""

from __future__ import annotations

from typing import IO, Any, Callable, Iterable, Mapping, MutableMapping
from urllib.parse import quote as urlencode
from urllib.parse import urljoin

import requests
from attrs import field, frozen
from requests.cookies import RequestsCookieJar
from typing_extensions import Literal


@frozen(init=False)
class ApiClient:
    """A Wrapper around [requests.Session][] with extra features for REST API calls.

    Additional features compared to using a [requests.Session][] directly:

    - You must set a root url at creation time, which then allows passing relative urls at request time.
    - It may also raise exceptions instead of returning error responses.
    - You can also pass additional kwargs at init time, which will be used to configure the
    [Session][requests.Session], instead of setting them later.
    - for parameters passed as `json`, `params` or `data`, values that are `None` can be
    automatically discarded from the request
    - boolean values in `data` or `params` fields can be serialized to values that are suitable
    for the target API, like `"true"`  or `"false"`, or `"1"` / `"0"`, instead of the default
    values `"True"` or `"False"`.

    `base_url` will serve as root for relative urls passed to
    [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request],
    [ApiClient.get()][requests_oauth2client.api_client.ApiClient.get], etc.

    An `HTTPError` will be raised everytime an API call returns an error code (>= 400), unless
    you set `raise_for_status` to `False`. Additional parameters passed at init time, including
    `auth` will be used to configure the [Session][requests.Session].

    Usage:
        ```python
        from requests_oauth2client import ApiClient

        api = ApiClient("https://myapi.local/resource", timeout=10)
        resp = api.get("/myid")  # this will send a GET request
        # to https://myapi.local/resource/myid

        # you can pass an underlying requests.Session at init time
        session = requests.Session()
        session.proxies = {"https": "https://localhost:3128"}
        api = ApiClient("https://myapi.local/resource", session=session)

        # or you can let ApiClient init its own session and provide additional configuration
        # parameters:
        api = ApiClient(
            "https://myapi.local/resource",
            proxies={"https": "https://localhost:3128"},
        )
        ```

    Args:
        base_url: the base api url, that is the root for all the target API endpoints.
        auth: the [requests.auth.AuthBase][] to use as authentication handler.
        timeout: the default timeout, in seconds, to use for each request from this `ApiClient`.
            Can be set to `None` to disable timeout.
        raise_for_status: if `True`, exceptions will be raised everytime a request returns an
            error code (>= 400).
        none_fields: what to do with parameters with value `None` in `data` or `json` fields.

            - if `"exclude"` (default), fields whose values are `None` are not included in the request.
            - if `"include"`, they are included with string value `None`. Note that this is
            the default behavior of `requests`.
            - if "empty", they are included with an empty value (as an empty string).
        bool_fields: a tuple of (true_value, false_value). Fields from `data` or `params` with
            a boolean value (`True` or `False`) will be serialized to the corresponding value.
            This can be useful since some APIs expect a `'true'` or `'false'` value as boolean,
            and `requests` serializes `True` to `'True'` and `False` to `'False'`.
            Set it to `None` to restore default requests behaviour.
        session: a preconfigured `requests.Session` to use with this `ApiClient`.
        **session_kwargs: additional kwargs to configure the underlying `requests.Session`.

    """

    base_url: str
    auth: requests.auth.AuthBase | None = None
    timeout: int | None = 60
    raise_for_status: bool = True
    none_fields: Literal["include", "exclude", "empty"] = "exclude"
    bool_fields: tuple[Any, Any] | None = "true", "false"
    session: requests.Session = field(factory=requests.Session)

    def __init__(
        self,
        base_url: str,
        *,
        auth: requests.auth.AuthBase | None = None,
        timeout: int | None = 60,
        raise_for_status: bool = True,
        none_fields: Literal["include", "exclude", "empty"] = "exclude",
        bool_fields: tuple[Any, Any] | None = ("true", "false"),
        session: requests.Session | None = None,
        **session_kwargs: Any,
    ):
        session = session or requests.Session()
        for key, val in session_kwargs.items():
            setattr(session, key, val)

        if bool_fields is None:
            bool_fields = (True, False)

        self.__attrs_init__(
            base_url=base_url,
            auth=auth,
            raise_for_status=raise_for_status,
            none_fields=none_fields,
            bool_fields=bool_fields,
            timeout=timeout,
            session=session,
        )

    def request(  # noqa: C901, PLR0913, D417
        self,
        method: str,
        url: None | str | bytes | Iterable[str | bytes | int] = None,
        *,
        params: None | bytes | MutableMapping[str, str] = None,
        data: (
            Iterable[bytes]
            | str
            | bytes
            | list[tuple[Any, Any]]
            | tuple[tuple[Any, Any], ...]
            | Mapping[Any, Any]
            | None
        ) = None,
        headers: MutableMapping[str, str] | None = None,
        cookies: None | RequestsCookieJar | MutableMapping[str, str] = None,
        files: MutableMapping[str, IO[Any]] | None = None,
        auth: (
            None
            | tuple[str, str]
            | requests.auth.AuthBase
            | Callable[[requests.PreparedRequest], requests.PreparedRequest]
        ) = None,
        timeout: None | float | tuple[float, float] | tuple[float, None] = None,
        allow_redirects: bool = False,
        proxies: MutableMapping[str, str] | None = None,
        hooks: None
        | (
            MutableMapping[
                str,
                (Iterable[Callable[[requests.Response], Any]] | Callable[[requests.Response], Any]),
            ]
        ) = None,
        stream: bool | None = None,
        verify: str | bool | None = None,
        cert: str | tuple[str, str] | None = None,
        json: Mapping[str, Any] | None = None,
        raise_for_status: bool | None = None,
        none_fields: Literal["include", "exclude", "empty"] | None = None,
        bool_fields: tuple[Any, Any] | None = None,
    ) -> requests.Response:
        """Overridden `request` method with extra features.

        Features added compared to plain request():

        - takes a relative path instead of a full url, which will be appended to the
          base_url
        - it can raise an exception when the API returns a non-success status code
        - allow_redirects is False by default (since API usually don't use redirects)
        - `data` or `json` fields with value `None` can either be included or excluded from the
          request
        - boolean fields can be serialized to `'true'` or `'false'` instead of `'True'` and
          `'False'`

        Args:
          method: the HTTP method to use
          url: the url where the request will be sent to. Can be a path, as str ;
            that path will be joined to the configured API url. Can also be an iterable of path
            segments, that will be joined to the root url.
          raise_for_status: like the parameter of the same name from `ApiClient.__init__`,
            but this will be applied for this request only.
          none_fields: like the parameter of the same name from `ApiClient.__init__`,
            but this will be applied for this request only.
          bool_fields: like the parameter of the same name from `ApiClient.__init__`,
            but this will be applied for this request only.

        Returns:
          a [requests.Response][] as returned by requests

        """
        url = self.to_absolute_url(url)

        if none_fields is None:
            none_fields = self.none_fields

        if none_fields == "exclude":
            if isinstance(data, Mapping):
                data = {key: val for key, val in data.items() if val is not None}
            if isinstance(json, Mapping):
                json = {key: val for key, val in json.items() if val is not None}
        elif none_fields == "empty":
            if isinstance(data, Mapping):
                data = {key: val if val is not None else "" for key, val in data.items()}
            if isinstance(json, Mapping):
                json = {key: val if val is not None else "" for key, val in json.items()}

        if bool_fields is None:
            bool_fields = self.bool_fields

        if bool_fields:
            try:
                true_value, false_value = bool_fields
            except ValueError:
                msg = "Invalid value for 'bool_fields'. Must be a 2 value tuple, with (true_value, false_value)."
                raise ValueError(msg) from None
            if isinstance(data, MutableMapping):
                for key, val in data.items():
                    if val is True:
                        data[key] = true_value
                    elif val is False:
                        data[key] = false_value
            if isinstance(params, MutableMapping):
                for key, val in params.items():
                    if val is True:
                        params[key] = true_value
                    elif val is False:
                        params[key] = false_value

        timeout = timeout or self.timeout

        response = self.session.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
            files=files,
            auth=auth or self.auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert,
            json=json,
        )

        if raise_for_status is None:
            raise_for_status = self.raise_for_status
        if raise_for_status:
            response.raise_for_status()
        return response

    def to_absolute_url(self, relative_url: None | str | bytes | Iterable[str | bytes | int] = None) -> str:
        """Convert a relative url to an absolute url.

        Given a `relative_url`, return the matching absolute url, based on the `base_url` that is
        configured for this API.

        The result of this method is different from a standard `urljoin()`, because a relative_url
        that starts with a "/" will not override the path from the base url. You can also pass an
        iterable of path parts as relative url, which will be properly joined with "/". Those parts
        may be `str` (which will be urlencoded) or `bytes` (which will be decoded as UTF-8 first) or
        any other type (which will be converted to `str` first, using the `str() function`). See the
        table below for example results which would exhibit most cases:

        | base_url | relative_url | result_url |
        |---------------------------|-----------------------------|-------------------------------------------|
        | "https://myhost.com/root" | "/path" | "https://myhost.com/root/path" |
        | "https://myhost.com/root" | "/path" | "https://myhost.com/root/path" |
        | "https://myhost.com/root" | b"/path" | "https://myhost.com/root/path" |
        | "https://myhost.com/root" | "path" | "https://myhost.com/root/path" |
        | "https://myhost.com/root" | None | "https://myhost.com/root" |
        | "https://myhost.com/root" |  ("user", 1, "resource") | "https://myhost.com/root/user/1/resource" |
        | "https://myhost.com/root" | "https://otherhost.org/foo" | ValueError |

        Args:
          relative_url: a relative url

        Returns:
          the resulting absolute url

        """
        url = relative_url

        if self.base_url:
            if url is not None:
                if not isinstance(url, (str, bytes)):
                    try:
                        url = "/".join(
                            [urlencode(part.decode() if isinstance(part, bytes) else str(part)) for part in url if part]
                        )
                    except Exception as exc:
                        msg = (
                            "Unexpected url type, please pass a relative path as string or"
                            " bytes, or an iterable of string-able objects"
                        )
                        raise TypeError(
                            msg,
                            type(url),
                        ) from exc

                if isinstance(url, bytes):
                    url = url.decode()

                if "://" in url:
                    msg = "url must be relative to root_url"
                    raise ValueError(msg)

                url = urljoin(self.base_url + "/", url.lstrip("/"))
            else:
                url = self.base_url

        if url is None or not isinstance(url, str):
            msg = "Unable to determine an absolute url."
            raise ValueError(msg)

        return url

    def get(
        self,
        url: None | str | bytes | Iterable[str | bytes | int] = None,
        raise_for_status: bool | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a GET request. Return a [Response][requests.Response] object.

        The passed `url` may be relative to the url passed at initialization time. It takes the same
        parameters as [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request].

        Args:
            url: a url where the request will be sent.
            raise_for_status: overrides the `raises_for_status` parameter passed at initialization time.
            **kwargs: Optional arguments that [request()][requests.request] takes.

        Returns:
            a [Response][requests.Response] object.

        Raises:
            requests.HTTPError: if `raises_for_status` is `True` and an error response is returned.

        """
        return self.request("GET", url, raise_for_status=raise_for_status, **kwargs)

    def post(
        self,
        url: str | bytes | Iterable[str | bytes] | None = None,
        raise_for_status: bool | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a POST request. Return a [Response][requests.Response] object.

        The passed `url` may be relative to the url passed at initialization time. It takes the same
        parameters as [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request].

        Args:
          url: an url where the request will be sent.
          raise_for_status: overrides the `raises_for_status` parameter passed at initialization time.
          **kwargs: Optional arguments that ``request`` takes.

        Returns:
          a [Response][requests.Response] object.

        Raises:
          requests.HTTPError: if `raises_for_status` is `True` and an error response is returned.

        """
        return self.request("POST", url, raise_for_status=raise_for_status, **kwargs)

    def patch(
        self,
        url: str | bytes | Iterable[str | bytes] | None = None,
        raise_for_status: bool | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a PATCH request. Return a [Response][requests.Response] object.

        The passed `url` may be relative to the url passed at initialization time. It takes the same
        parameters as [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request].

        Args:
          url: an url where the request will be sent.
          raise_for_status: overrides the `raises_for_status` parameter passed at initialization time.
          **kwargs: Optional arguments that ``request`` takes.

        Returns:
          a [Response][requests.Response] object.

        Raises:
          requests.HTTPError: if `raises_for_status` is `True` and an error response is returned.

        """
        return self.request("PATCH", url, raise_for_status=raise_for_status, **kwargs)

    def put(
        self,
        url: str | bytes | Iterable[str | bytes] | None = None,
        raise_for_status: bool | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a PUT request. Return a [Response][requests.Response] object.

        The passed `url` may be relative to the url passed at initialization time. It takes the same
        parameters as [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request].

        Args:
          url: a url where the request will be sent.
          raise_for_status: overrides the `raises_for_status` parameter passed at initialization time.
          **kwargs: additional kwargs for `requests.request()`

        Returns:
          a [Response][requests.Response] object.

        Raises:
          requests.HTTPError: if `raises_for_status` is `True` and an error response is returned.

        """
        return self.request("PUT", url, raise_for_status=raise_for_status, **kwargs)

    def delete(
        self,
        url: str | bytes | Iterable[str | bytes] | None = None,
        raise_for_status: bool | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a DELETE request. Return a [Response][requests.Response] object.

        The passed `url` may be relative to the url passed at initialization time. It takes the same
        parameters as [ApiClient.request()][requests_oauth2client.api_client.ApiClient.request].

        Args:
          url: a url where the request will be sent.
          raise_for_status: overrides the `raises_for_status` parameter passed at initialization time.
          **kwargs: additional kwargs for `requests.request()`.

        Returns:
          a [Response][requests.Response] object.

        Raises:
          requests.HTTPError: if `raises_for_status` is `True` and an error response is returned.

        """
        return self.request("DELETE", url, raise_for_status=raise_for_status, **kwargs)

    def __getattr__(self, item: str) -> ApiClient:
        """Allow access sub resources with an attribute-based syntax.

        Args:
            item: a subpath

        Returns:
            a new ApiClient initialised on the new base url

        Usage:
            ```python
            from requests_oauth2client import ApiClient

            api = ApiClient("https://myapi.local")
            resource1 = api.resource1.get()  # GET https://myapi.local/resource1
            resource2 = api.resource2.get()  # GET https://myapi.local/resource2
            ```

        """
        return self[item]

    def __getitem__(self, item: str) -> ApiClient:
        """Allow access to sub resources with a subscription-based syntax.

        Args:
            item: a subpath

        Returns:
            a new ApiClient initialised on the new base url

        Usage:
            ```python
            from requests_oauth2client import ApiClient

            api = ApiClient("https://myapi.local")
            resource1 = api["resource1"].get()  # GET https://myapi.local/resource1
            resource2 = api["resource2"].get()  # GET https://myapi.local/resource2
            ```

        """
        new_base_uri = self.to_absolute_url(item)
        return ApiClient(
            new_base_uri,
            session=self.session,
            none_fields=self.none_fields,
            bool_fields=self.bool_fields,
            timeout=self.timeout,
            raise_for_status=self.raise_for_status,
        )

    def __enter__(self) -> ApiClient:
        """Allow `ApiClient` to act as a context manager.

        You can then use an `ApiClient` instance in a `with` clause, the same way as
        `requests.Session`. The underlying request.Session will be closed on exit.

        Usage:
            ```python
            with ApiClient("https://myapi.com/path") as client:
                resp = client.get("resource")
            ```

        """
        return self

    def __exit__(self, *args: Any) -> None:
        """Close the underlying requests.Session on exit."""
        self.session.close()
