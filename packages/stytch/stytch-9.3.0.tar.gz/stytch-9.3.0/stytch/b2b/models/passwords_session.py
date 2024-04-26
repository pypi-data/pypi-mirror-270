# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class ResetRequestLocale(str, enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ResetResponse(ResponseBase):
    """Response type for `Sessions.reset`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session. The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms), [TOTP Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-totp), or [Recovery Codes Recover endpoint](https://stytch.com/docs/b2b/api/recovery-codes-recover) to complete an MFA flow and log in to the Organization. It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token; or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
    session_token: str
    session_jwt: str
    intermediate_session_token: str
    member_authenticated: bool
    member_session: Optional[MemberSession] = None
    mfa_required: Optional[MfaRequired] = None
