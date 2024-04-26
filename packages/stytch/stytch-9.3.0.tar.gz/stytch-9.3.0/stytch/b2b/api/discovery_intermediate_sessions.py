# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.b2b.models.discovery_intermediate_sessions import (
    ExchangeRequestLocale,
    ExchangeResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class IntermediateSessions:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def exchange(
        self,
        intermediate_session_token: str,
        organization_id: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        locale: Optional[Union[ExchangeRequestLocale, str]] = None,
    ) -> ExchangeResponse:
        """Exchange an Intermediate Session for a fully realized [Member Session](https://stytch.com/docs/b2b/api/session-object) in a desired [Organization](https://stytch.com/docs/b2b/api/organization-object).
        This operation consumes the Intermediate Session.

        This endpoint can be used to accept invites and create new members via domain matching.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`.
        The `intermediate_session_token` will not be consumed and instead will be returned in the response.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
            "organization_id": organization_id,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for(
            "/v1/b2b/discovery/intermediate_sessions/exchange", data
        )
        res = self.sync_client.post(url, data, headers)
        return ExchangeResponse.from_json(res.response.status_code, res.json)

    async def exchange_async(
        self,
        intermediate_session_token: str,
        organization_id: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        locale: Optional[ExchangeRequestLocale] = None,
    ) -> ExchangeResponse:
        """Exchange an Intermediate Session for a fully realized [Member Session](https://stytch.com/docs/b2b/api/session-object) in a desired [Organization](https://stytch.com/docs/b2b/api/organization-object).
        This operation consumes the Intermediate Session.

        This endpoint can be used to accept invites and create new members via domain matching.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`.
        The `intermediate_session_token` will not be consumed and instead will be returned in the response.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `intermediate_session_token` can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to join a different Organization or create a new one.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        Fields:
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "intermediate_session_token": intermediate_session_token,
            "organization_id": organization_id,
        }
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for(
            "/v1/b2b/discovery/intermediate_sessions/exchange", data
        )
        res = await self.async_client.post(url, data, headers)
        return ExchangeResponse.from_json(res.response.status, res.json)
