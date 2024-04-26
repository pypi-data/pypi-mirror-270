# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import List, Optional

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class GetResponse(ResponseBase):
    """Response type for `RecoveryCodes.get`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - recovery_codes: An array of recovery codes that can be used to recover a Member's account.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
    recovery_codes: List[str]


class RecoverResponse(ResponseBase):
    """Response type for `RecoveryCodes.recover`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - recovery_codes_remaining: The number of recovery codes remaining for a Member.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
    session_token: str
    session_jwt: str
    recovery_codes_remaining: int
    member_session: Optional[MemberSession] = None


class RotateResponse(ResponseBase):
    """Response type for `RecoveryCodes.rotate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object)
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - recovery_codes: An array of recovery codes that can be used to recover a Member's account.
    """  # noqa

    member_id: str
    member: Member
    organization: Organization
    recovery_codes: List[str]
