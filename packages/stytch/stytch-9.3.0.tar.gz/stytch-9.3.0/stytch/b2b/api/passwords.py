# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from stytch.b2b.api.passwords_email import Email
from stytch.b2b.api.passwords_existing_password import ExistingPassword
from stytch.b2b.api.passwords_session import Sessions
from stytch.b2b.models.passwords import (
    AuthenticateRequestLocale,
    AuthenticateResponse,
    MigrateRequestHashType,
    MigrateResponse,
    StrengthCheckResponse,
)
from stytch.consumer.models.passwords import (
    Argon2Config,
    MD5Config,
    PBKDF2Config,
    ScryptConfig,
    SHA1Config,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Passwords:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.email = Email(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.sessions = Sessions(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )
        self.existing_password = ExistingPassword(
            api_base=self.api_base,
            sync_client=self.sync_client,
            async_client=self.async_client,
        )

    def strength_check(
        self,
        password: str,
        email_address: Optional[str] = None,
    ) -> StrengthCheckResponse:
        """This API allows you to check whether the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

        This endpoint adapts to your Project's password strength configuration. If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the default, your passwords are considered valid if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), your passwords are considered valid if they meet the requirements that you've set with Stytch. You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        ## Password feedback
        The zxcvbn_feedback and luds_feedback objects contains relevant fields for you to relay feedback to users that failed to create a strong enough password.

        If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the feedback object will contain warning and suggestions for any password that does not meet the [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy) strength requirements. You can return these strings directly to the user to help them craft a strong password.

        If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), the feedback object will contain a collection of fields that the user failed or passed. You'll want to prompt the user to create a password that meets all requirements that they failed.

        Fields:
          - password: The password to authenticate.
          - email_address: The email address of the Member.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "password": password,
        }
        if email_address is not None:
            data["email_address"] = email_address

        url = self.api_base.url_for("/v1/b2b/passwords/strength_check", data)
        res = self.sync_client.post(url, data, headers)
        return StrengthCheckResponse.from_json(res.response.status_code, res.json)

    async def strength_check_async(
        self,
        password: str,
        email_address: Optional[str] = None,
    ) -> StrengthCheckResponse:
        """This API allows you to check whether the user’s provided password is valid, and to provide feedback to the user on how to increase the strength of their password.

        This endpoint adapts to your Project's password strength configuration. If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the default, your passwords are considered valid if the strength score is >= 3. If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), your passwords are considered valid if they meet the requirements that you've set with Stytch. You may update your password strength configuration in the [stytch dashboard](https://stytch.com/dashboard/password-strength-config).

        ## Password feedback
        The zxcvbn_feedback and luds_feedback objects contains relevant fields for you to relay feedback to users that failed to create a strong enough password.

        If you're using [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy), the feedback object will contain warning and suggestions for any password that does not meet the [zxcvbn](https://stytch.com/docs/guides/passwords/strength-policy) strength requirements. You can return these strings directly to the user to help them craft a strong password.

        If you're using [LUDS](https://stytch.com/docs/guides/passwords/strength-policy), the feedback object will contain a collection of fields that the user failed or passed. You'll want to prompt the user to create a password that meets all requirements that they failed.

        Fields:
          - password: The password to authenticate.
          - email_address: The email address of the Member.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "password": password,
        }
        if email_address is not None:
            data["email_address"] = email_address

        url = self.api_base.url_for("/v1/b2b/passwords/strength_check", data)
        res = await self.async_client.post(url, data, headers)
        return StrengthCheckResponse.from_json(res.response.status, res.json)

    def migrate(
        self,
        email_address: str,
        hash: str,
        hash_type: Union[MigrateRequestHashType, str],
        organization_id: str,
        md_5_config: Optional[MD5Config] = None,
        argon_2_config: Optional[Argon2Config] = None,
        sha_1_config: Optional[SHA1Config] = None,
        scrypt_config: Optional[ScryptConfig] = None,
        pbkdf_2_config: Optional[PBKDF2Config] = None,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        roles: Optional[List[str]] = None,
        preserve_existing_sessions: Optional[bool] = None,
    ) -> MigrateResponse:
        """Adds an existing password to a member's email that doesn't have a password yet. We support migrating members from passwords stored with bcrypt, scrypt, argon2, MD-5, SHA-1, and PBKDF2. This endpoint has a rate limit of 100 requests per second.

        Fields:
          - email_address: The email address of the Member.
          - hash: The password hash. For a Scrypt or PBKDF2 hash, the hash needs to be a base64 encoded string.
          - hash_type: The password hash used. Currently `bcrypt`, `scrypt`, `argon2i`, `argon2id`, `md_5`, `sha_1`, and `pbkdf_2` are supported.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - md_5_config: Optional parameters for MD-5 hash types.
          - argon_2_config: Required parameters if the argon2 hex form, as opposed to the encoded form, is supplied.
          - sha_1_config: Optional parameters for SHA-1 hash types.
          - scrypt_config: Required parameters if the scrypt is not provided in a **PHC encoded form**.
          - pbkdf_2_config: Required additional parameters for PBKDF2 hash keys. Note that we use the SHA-256 by default, please contact [support@stytch.com](mailto:support@stytch.com) if you use another hashing function.
          - name: The name of the Member. Each field in the name object is optional.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - roles: Roles to explicitly assign to this Member.
         Will completely replace any existing explicitly assigned roles. See the
         [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.

           If a Role is removed from a Member, and the Member is also implicitly assigned this Role from an SSO connection
           or an SSO group, we will by default revoke any existing sessions for the Member that contain any SSO
           authentication factors with the affected connection ID. You can preserve these sessions by passing in the
           `preserve_existing_sessions` parameter with a value of `true`.
          - preserve_existing_sessions: Whether to preserve existing sessions when explicit Roles that are revoked are also implicitly assigned
          by SSO connection or SSO group. Defaults to `false` - that is, existing Member Sessions that contain SSO
          authentication factors with the affected SSO connection IDs will be revoked.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
            "organization_id": organization_id,
        }
        if md_5_config is not None:
            data["md_5_config"] = md_5_config.dict()
        if argon_2_config is not None:
            data["argon_2_config"] = argon_2_config.dict()
        if sha_1_config is not None:
            data["sha_1_config"] = sha_1_config.dict()
        if scrypt_config is not None:
            data["scrypt_config"] = scrypt_config.dict()
        if pbkdf_2_config is not None:
            data["pbkdf_2_config"] = pbkdf_2_config.dict()
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if roles is not None:
            data["roles"] = roles
        if preserve_existing_sessions is not None:
            data["preserve_existing_sessions"] = preserve_existing_sessions

        url = self.api_base.url_for("/v1/b2b/passwords/migrate", data)
        res = self.sync_client.post(url, data, headers)
        return MigrateResponse.from_json(res.response.status_code, res.json)

    async def migrate_async(
        self,
        email_address: str,
        hash: str,
        hash_type: MigrateRequestHashType,
        organization_id: str,
        md_5_config: Optional[MD5Config] = None,
        argon_2_config: Optional[Argon2Config] = None,
        sha_1_config: Optional[SHA1Config] = None,
        scrypt_config: Optional[ScryptConfig] = None,
        pbkdf_2_config: Optional[PBKDF2Config] = None,
        name: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
        roles: Optional[List[str]] = None,
        preserve_existing_sessions: Optional[bool] = None,
    ) -> MigrateResponse:
        """Adds an existing password to a member's email that doesn't have a password yet. We support migrating members from passwords stored with bcrypt, scrypt, argon2, MD-5, SHA-1, and PBKDF2. This endpoint has a rate limit of 100 requests per second.

        Fields:
          - email_address: The email address of the Member.
          - hash: The password hash. For a Scrypt or PBKDF2 hash, the hash needs to be a base64 encoded string.
          - hash_type: The password hash used. Currently `bcrypt`, `scrypt`, `argon2i`, `argon2id`, `md_5`, `sha_1`, and `pbkdf_2` are supported.
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - md_5_config: Optional parameters for MD-5 hash types.
          - argon_2_config: Required parameters if the argon2 hex form, as opposed to the encoded form, is supplied.
          - sha_1_config: Optional parameters for SHA-1 hash types.
          - scrypt_config: Required parameters if the scrypt is not provided in a **PHC encoded form**.
          - pbkdf_2_config: Required additional parameters for PBKDF2 hash keys. Note that we use the SHA-256 by default, please contact [support@stytch.com](mailto:support@stytch.com) if you use another hashing function.
          - name: The name of the Member. Each field in the name object is optional.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
          frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
          for complete field behavior details.
          - roles: Roles to explicitly assign to this Member.
         Will completely replace any existing explicitly assigned roles. See the
         [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.

           If a Role is removed from a Member, and the Member is also implicitly assigned this Role from an SSO connection
           or an SSO group, we will by default revoke any existing sessions for the Member that contain any SSO
           authentication factors with the affected connection ID. You can preserve these sessions by passing in the
           `preserve_existing_sessions` parameter with a value of `true`.
          - preserve_existing_sessions: Whether to preserve existing sessions when explicit Roles that are revoked are also implicitly assigned
          by SSO connection or SSO group. Defaults to `false` - that is, existing Member Sessions that contain SSO
          authentication factors with the affected SSO connection IDs will be revoked.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
            "organization_id": organization_id,
        }
        if md_5_config is not None:
            data["md_5_config"] = md_5_config.dict()
        if argon_2_config is not None:
            data["argon_2_config"] = argon_2_config.dict()
        if sha_1_config is not None:
            data["sha_1_config"] = sha_1_config.dict()
        if scrypt_config is not None:
            data["scrypt_config"] = scrypt_config.dict()
        if pbkdf_2_config is not None:
            data["pbkdf_2_config"] = pbkdf_2_config.dict()
        if name is not None:
            data["name"] = name
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            data["untrusted_metadata"] = untrusted_metadata
        if roles is not None:
            data["roles"] = roles
        if preserve_existing_sessions is not None:
            data["preserve_existing_sessions"] = preserve_existing_sessions

        url = self.api_base.url_for("/v1/b2b/passwords/migrate", data)
        res = await self.async_client.post(url, data, headers)
        return MigrateResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        organization_id: str,
        email_address: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        locale: Optional[Union[AuthenticateRequestLocale, str]] = None,
        intermediate_session_token: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a member with their email address and password. This endpoint verifies that the member has a password currently set, and that the entered password is correct.

        If you have breach detection during authentication enabled in your [password strength policy](https://stytch.com/docs/b2b/guides/passwords/strength-policies) and the member's credentials have appeared in the HaveIBeenPwned dataset, this endpoint will return a `member_reset_password` error even if the member enters a correct password. We force a password reset in this case to ensure that the member is the legitimate owner of the email address and not a malicious actor abusing the compromised credentials.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        If a valid `session_token` or `session_jwt` is passed in, the Member will not be required to complete an MFA step.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - password: The password to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - intermediate_session_token: Adds this primary authentication factor to the intermediate session token. If the resulting set of factors satisfies the organization's primary authentication requirements and MFA requirements, the intermediate session token will be consumed and converted to a member session. If not, the same intermediate session token will be returned.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if locale is not None:
            data["locale"] = locale
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token

        url = self.api_base.url_for("/v1/b2b/passwords/authenticate", data)
        res = self.sync_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        organization_id: str,
        email_address: str,
        password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        locale: Optional[AuthenticateRequestLocale] = None,
        intermediate_session_token: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticate a member with their email address and password. This endpoint verifies that the member has a password currently set, and that the entered password is correct.

        If you have breach detection during authentication enabled in your [password strength policy](https://stytch.com/docs/b2b/guides/passwords/strength-policies) and the member's credentials have appeared in the HaveIBeenPwned dataset, this endpoint will return a `member_reset_password` error even if the member enters a correct password. We force a password reset in this case to ensure that the member is the legitimate owner of the email address and not a malicious actor abusing the compromised credentials.

        If the Member is required to complete MFA to log in to the Organization, the returned value of `member_authenticated` will be `false`, and an `intermediate_session_token` will be returned.
        The `intermediate_session_token` can be passed into the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA step and acquire a full member session.
        The `session_duration_minutes` and `session_custom_claims` parameters will be ignored.

        If a valid `session_token` or `session_jwt` is passed in, the Member will not be required to complete an MFA step.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - email_address: The email address of the Member.
          - password: The password to authenticate.
          - session_token: A secret token for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - locale: If the Member needs to complete an MFA step, and the Member has a phone number, this endpoint will pre-emptively send a one-time passcode (OTP) to the Member's phone number. The locale argument will be used to determine which language to use when sending the passcode.

        Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - intermediate_session_token: Adds this primary authentication factor to the intermediate session token. If the resulting set of factors satisfies the organization's primary authentication requirements and MFA requirements, the intermediate session token will be consumed and converted to a member session. If not, the same intermediate session token will be returned.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if locale is not None:
            data["locale"] = locale
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token

        url = self.api_base.url_for("/v1/b2b/passwords/authenticate", data)
        res = await self.async_client.post(url, data, headers)
        return AuthenticateResponse.from_json(res.response.status, res.json)
