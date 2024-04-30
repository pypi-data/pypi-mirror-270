# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    state: Required[Literal["active", "blocked"]]
    """State to update the account, it can be one of the following values:

    - active: it's enabled to perform operations with the account balance.
    - blocked: it's disabled by a tenant and couldn't perform any operation with the
      account balance.
    """

    detail: str
    """
    It provides a textual reason why the account is blocked in case of the
    state_reason value is `other`.
    """

    reason: Literal["temporary", "user_request", "unused", "fraud", "other"]
    """It provides the reason why the account could be blocked.

    It is required when the account is transitioned to being blocked.
    """
