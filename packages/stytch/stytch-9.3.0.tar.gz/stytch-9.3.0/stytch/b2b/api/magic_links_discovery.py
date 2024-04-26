# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.magic_links_discovery import AuthenticateResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Discovery:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def authenticate(
        self,
        discovery_magic_links_token: str,
        pkce_code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticates the Discovery Magic Link token and exchanges it for an Intermediate Session Token. Intermediate Session Tokens can be used for various Discovery login flows and are valid for 10 minutes.

        Fields:
          - discovery_magic_links_token: The Discovery Email Magic Link token to authenticate.
          - pkce_code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "discovery_magic_links_token": discovery_magic_links_token,
        }
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier

        url = self.api_base.url_for("/v1/b2b/magic_links/discovery/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        discovery_magic_links_token: str,
        pkce_code_verifier: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticates the Discovery Magic Link token and exchanges it for an Intermediate Session Token. Intermediate Session Tokens can be used for various Discovery login flows and are valid for 10 minutes.

        Fields:
          - discovery_magic_links_token: The Discovery Email Magic Link token to authenticate.
          - pkce_code_verifier: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "discovery_magic_links_token": discovery_magic_links_token,
        }
        if pkce_code_verifier is not None:
            data["pkce_code_verifier"] = pkce_code_verifier

        url = self.api_base.url_for("/v1/b2b/magic_links/discovery/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)
