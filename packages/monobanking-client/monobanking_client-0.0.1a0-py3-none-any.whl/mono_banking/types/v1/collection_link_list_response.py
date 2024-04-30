# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CollectionLinkListResponse",
    "CollectionLink",
    "CollectionLinkAmount",
    "CollectionLinkPayer",
    "CollectionLinkPayerNote",
    "CollectionLinkReference",
    "Pagination",
]


class CollectionLinkAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class CollectionLinkPayerNote(BaseModel):
    editable: bool
    """Allows to payer to edit the note field"""

    required: bool
    """Requires to payer to fill the note field"""

    value: Optional[str] = None
    """Sets a note value to be preloaded in the checkout form"""


class CollectionLinkPayer(BaseModel):
    document_number: Optional[str] = None
    """
    Sets the payer's document number, which will be preloaded into the checkout
    form. This field is alphanumeric, only accepts letters and numbers.
    """

    document_type: Optional[
        Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]
    ] = None
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

    email: Optional[str] = None
    """Sets the payer's email, which will be preloaded into the checkout form"""

    name: Optional[str] = None
    """Sets the payer's full name, which will be preloaded into the checkout form"""

    phone: Optional[str] = None
    """Sets the payer's phone number, which will be preloaded into the checkout form"""

    note: Optional[CollectionLinkPayerNote] = None
    """Sets the note field in the checkout form.

    When there is no note, and it is configured not to be editable, the checkout
    form's note field will not be visible.
    """


class CollectionLinkReference(BaseModel):
    editable: bool
    """Allows to payer to edit the reference field"""

    required: bool
    """Requires to payer to fill the reference field"""

    value: Optional[str] = None
    """Prefill the reference field into the form"""


class CollectionLink(BaseModel):
    account_id: str
    """Indicates the format for resource's ID"""

    amount: CollectionLinkAmount
    """Money schema"""

    amount_validation: Literal["free", "fixed", "can_be_less", "can_be_greater"]
    """Sets the collection link validations of the `amount` field.

    Two validations will always be present in the checkout form `amount` field:

    1. The amount must be greater than zero.
    2. The amount must be within the limits allowed by Mono.

    The field "amount_validation" is an additional validation configured to be
    applied to the checkout form's amount field.

    - fixed: No validation will be applied to the amount field in the checkout form,
      and the user will not be able to enter an amount. The checkout form's amount
      field will contain the configured amount (the amount is fixed).
    - free: No validation will be applied, and the user can enter any amount in the
      checkout form.
    - can_be_less: The amount entered by the user can be less than or equal to the
      configured amount.
    - can_be_greater: The amount entered by the user can be greater than or equal to
      the configured amount.
    """

    usage_type: Literal["single_use", "multi_use"]
    """Sets the collection link type. There are two types of collection links:

    1. single_use: As the name suggests, this type of collection link can only be
       used once. When a successful payment is made, the link will be disabled. The
       collection link will display a message if a user tries to access it again
       after the payment has been made.
    2. multi_use: As the name suggests, this type of collection link can be used
       multiple times
    """

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    enabled: Optional[bool] = None
    """Turns the collection link on or off."""

    expires_at: Optional[datetime] = None
    """
    Sets an expiration date and time for the collection link. If a user attempts to
    enter an expired link, a message will be displayed informing them that the link
    has expired.
    """

    external_id: Optional[str] = None
    """
    Associates the collection link with an external register. For example, this
    field may contain identifiers of entities that could be used in some external
    system.
    """

    inserted_at: Optional[datetime] = None
    """Indicates when a collection link was created"""

    link: Optional[str] = None
    """Contains the collection link URL"""

    payer: Optional[CollectionLinkPayer] = None
    """Sets the payer data, which will be preloaded into the checkout form.

    This payer data can be optional
    """

    redirect_url: Optional[str] = None
    """
    Sets a URL on the redirect button on the payment receipt after payment is made.
    The URL contains three parameters from the query string:

    1. id: this contains the same value as the field "external_id"
    2. clink_id: this is the collection link ID
    3. intent_id: this is the collection intent ID or the payment ID
    """

    reference: Optional[CollectionLinkReference] = None
    """Sets the reference field in the checkout form.

    When there is no reference, and it is configured not to be editable, the
    checkout form reference field will not be visible.
    """

    successful_payments: Optional[int] = None
    """Keeps a record of payments that were successfully processed."""

    updated_at: Optional[datetime] = None
    """Indicates when a collection link was updated"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class CollectionLinkListResponse(BaseModel):
    collection_links: Optional[List[CollectionLink]] = None
    """It contains a list with collection links"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
