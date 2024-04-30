# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BankListParams"]


class BankListParams(TypedDict, total=False):
    kind: Literal["transfers", "pse"]
    """
    there are two types of responses (Polymorphism response) the first `transfers`
    are the banks used by the bank transfers and the `pse` are the banks from the
    pse provider.
    """
