# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountHolderUpdateStateParams"]


class AccountHolderUpdateStateParams(TypedDict, total=False):
    state: Required[Literal["active", "blocked"]]
    """
    It represents the current state of the account holder, and these are the
    possible states of an account holder:

    - active: it is enable to manage and perform actions with its accounts.
    - blocked: it is blocked by the client, but you could also make it active again.
    """

    detail: str
    """
    It provides a textual reason why the account holder is blocked in case of the
    state_reason value is `other`.
    """

    reason: Literal["fraud", "user_request", "other"]
    """It provides the reason why the account holder could be blocked.

    It is required when the account holder is transitioned to being blocked.
    """
