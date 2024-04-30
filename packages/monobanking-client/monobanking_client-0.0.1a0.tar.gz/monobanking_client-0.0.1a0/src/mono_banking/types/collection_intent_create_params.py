# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionIntentCreateParams", "Amount", "Payer", "Payment"]


class CollectionIntentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Indicates the format for resource's ID"""

    amount: Required[Amount]
    """Money schema"""

    bank_code: Required[str]
    """Bank code used by PSE to make the collection"""

    ip: Required[str]
    """The user IP address"""

    payer: Required[Payer]

    payment: Required[Payment]

    redirect_url: Required[str]
    """
    The URL to redirect when the collection intent successfully completes through
    the provider.
    """

    note: Optional[str]
    """Note indicated by the user of the client"""

    reference: Optional[str]
    """Reference indicated by the client or by the user of the client"""


class Amount(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP"]]
    """Currency of money"""


class Payer(TypedDict, total=False):
    document_number: Required[str]
    """Document number of payer"""

    document_type: Required[
        Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]
    ]
    """The document types are represented by codes and can be:

    For Colombia:

    - CC
    - TI
    - NUIP
    - TE
    - CE
    - NIT
    - PASS
    - PEP
    - PPT
    - FDO
    - RC

    For other countries:

    - NID (National Identification)
    - DL (Driver License)
    - PASS
    """

    email: Required[str]
    """Payer email address"""

    name: Required[str]
    """Name of payer"""

    person_type: Required[Literal["natural", "legal"]]
    """The person types can be:

    - legal,
    - natural
    """

    phone_number: Required[str]
    """Payer phone number"""


class Payment(TypedDict, total=False):
    provider: Literal["pse"]
    """
    The providers of the collections are the intermediaries to facilitate the
    collection of the money. These are the current ones:

    - pse
    """
