# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CollectionIntentListResponse",
    "CollectionIntent",
    "CollectionIntentAmount",
    "CollectionIntentPayer",
    "CollectionIntentPayment",
    "Pagination",
]


class CollectionIntentAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class CollectionIntentPayer(BaseModel):
    document_number: str
    """Document number of payer"""

    document_type: Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]
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

    name: str
    """Name of payer"""


class CollectionIntentPayment(BaseModel):
    provider: Optional[Literal["pse"]] = None
    """
    The providers of the collections are the intermediaries to facilitate the
    collection of the money. These are the current ones:

    - pse
    """

    transaction_id: Optional[str] = None
    """
    The transaction ID with which you can identify the collection intent with the
    provider
    """

    url: Optional[str] = None
    """The URL of the provider that will be used to complete the collection intent"""


class CollectionIntent(BaseModel):
    account_id: str
    """Indicates the format for resource's ID"""

    amount: CollectionIntentAmount
    """Money schema"""

    payer: CollectionIntentPayer

    payment: CollectionIntentPayment

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    inserted_at: Optional[datetime] = None
    """Indicates when a resource is created"""

    note: Optional[str] = None
    """Note indicated by the user of the client"""

    reference: Optional[str] = None
    """Reference indicated by the client or by the user of the client"""

    state: Optional[Literal["created", "in_progress", "approved_in_provider", "account_credited", "failed"]] = None
    """
    - created: Represents when a payer completes and submits the payment form.
    - in_progress: Represents when the user is carrying out the payment process in
      the bank interface, the collection intent enters this state.
    - approved_in_provider: Remains in this state when the user has successfully
      completed the payment process, but the payment has not yet been credited.
    - account_credited: Means that the payment has already been credited to the
      customer's account balance.
    - failed: Occurs when the user could not finish the payment process.
    """

    updated_at: Optional[datetime] = None
    """Indicates when a resource is updated"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class CollectionIntentListResponse(BaseModel):
    collection_intents: Optional[List[CollectionIntent]] = None
    """List of collection intents"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
