# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.organizations_members_oauth_providers import (
    GoogleResponse,
    MicrosoftResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class OAuthProviders:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def google(
        self,
        organization_id: str,
        member_id: str,
        include_refresh_token: Optional[bool] = None,
    ) -> GoogleResponse:
        """Retrieve the saved Google access token and ID token for a member. After a successful OAuth login, Stytch will save the
        issued access token and ID token from the identity provider. If a refresh token has been issued, Stytch will refresh the
        access token automatically.

        __Note:__ Google does not issue a refresh token on every login, and refresh tokens may expire if unused.
        To force a refresh token to be issued, pass the `?provider_prompt=consent` query param into the
        [Start Google OAuth flow](https://stytch.com/docs/b2b/api/oauth-google-start) endpoint.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - include_refresh_token: Whether to return the refresh token Stytch has stored for the OAuth Provider. Defaults to false. **Important:** If your application exchanges the refresh token, Stytch may not be able to automatically refresh access tokens in the future.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if include_refresh_token is not None:
            data["include_refresh_token"] = include_refresh_token

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}/oauth_providers/google",
            data,
        )
        res = self.sync_client.get(url, data, headers)
        return GoogleResponse.from_json(res.response.status_code, res.json)

    async def google_async(
        self,
        organization_id: str,
        member_id: str,
        include_refresh_token: Optional[bool] = None,
    ) -> GoogleResponse:
        """Retrieve the saved Google access token and ID token for a member. After a successful OAuth login, Stytch will save the
        issued access token and ID token from the identity provider. If a refresh token has been issued, Stytch will refresh the
        access token automatically.

        __Note:__ Google does not issue a refresh token on every login, and refresh tokens may expire if unused.
        To force a refresh token to be issued, pass the `?provider_prompt=consent` query param into the
        [Start Google OAuth flow](https://stytch.com/docs/b2b/api/oauth-google-start) endpoint.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - include_refresh_token: Whether to return the refresh token Stytch has stored for the OAuth Provider. Defaults to false. **Important:** If your application exchanges the refresh token, Stytch may not be able to automatically refresh access tokens in the future.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if include_refresh_token is not None:
            data["include_refresh_token"] = include_refresh_token

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}/oauth_providers/google",
            data,
        )
        res = await self.async_client.get(url, data, headers)
        return GoogleResponse.from_json(res.response.status, res.json)

    def microsoft(
        self,
        organization_id: str,
        member_id: str,
        include_refresh_token: Optional[bool] = None,
    ) -> MicrosoftResponse:
        """Retrieve the saved Microsoft access token and ID token for a member. After a successful OAuth login, Stytch will save the
        issued access token and ID token from the identity provider. If a refresh token has been issued, Stytch will refresh the
        access token automatically.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - include_refresh_token: Whether to return the refresh token Stytch has stored for the OAuth Provider. Defaults to false. **Important:** If your application exchanges the refresh token, Stytch may not be able to automatically refresh access tokens in the future.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if include_refresh_token is not None:
            data["include_refresh_token"] = include_refresh_token

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}/oauth_providers/microsoft",
            data,
        )
        res = self.sync_client.get(url, data, headers)
        return MicrosoftResponse.from_json(res.response.status_code, res.json)

    async def microsoft_async(
        self,
        organization_id: str,
        member_id: str,
        include_refresh_token: Optional[bool] = None,
    ) -> MicrosoftResponse:
        """Retrieve the saved Microsoft access token and ID token for a member. After a successful OAuth login, Stytch will save the
        issued access token and ID token from the identity provider. If a refresh token has been issued, Stytch will refresh the
        access token automatically.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - include_refresh_token: Whether to return the refresh token Stytch has stored for the OAuth Provider. Defaults to false. **Important:** If your application exchanges the refresh token, Stytch may not be able to automatically refresh access tokens in the future.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if include_refresh_token is not None:
            data["include_refresh_token"] = include_refresh_token

        url = self.api_base.url_for(
            "/v1/b2b/organizations/{organization_id}/members/{member_id}/oauth_providers/microsoft",
            data,
        )
        res = await self.async_client.get(url, data, headers)
        return MicrosoftResponse.from_json(res.response.status, res.json)
