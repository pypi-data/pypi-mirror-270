# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CollectionLinkCreateParams", "Amount", "Payer", "PayerNote", "Reference"]


class CollectionLinkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Indicates the format for resource's ID"""

    amount: Required[Amount]
    """Money schema"""

    amount_validation: Required[Literal["free", "fixed", "can_be_less", "can_be_greater"]]
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

    usage_type: Required[Literal["single_use", "multi_use"]]
    """Sets the collection link type. There are two types of collection links:

    1. single_use: As the name suggests, this type of collection link can only be
       used once. When a successful payment is made, the link will be disabled. The
       collection link will display a message if a user tries to access it again
       after the payment has been made.
    2. multi_use: As the name suggests, this type of collection link can be used
       multiple times
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Sets an expiration date and time for the collection link. If a user attempts to
    enter an expired link, a message will be displayed informing them that the link
    has expired.
    """

    external_id: Optional[str]
    """
    Associates the collection link with an external register. For example, this
    field may contain identifiers of entities that could be used in some external
    system.
    """

    payer: Payer
    """Sets the payer data, which will be preloaded into the checkout form.

    This payer data can be optional
    """

    redirect_url: Optional[str]
    """
    Sets a URL on the redirect button on the payment receipt after payment is made.
    The URL contains three parameters from the query string:

    1. id: this contains the same value as the field "external_id"
    2. clink_id: this is the collection link ID
    3. intent_id: this is the collection intent ID or the payment ID
    """

    reference: Reference
    """Sets the reference field in the checkout form.

    When there is no reference, and it is configured not to be editable, the
    checkout form reference field will not be visible.
    """


class Amount(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP"]]
    """Currency of money"""


class PayerNote(TypedDict, total=False):
    editable: Required[bool]
    """Allows to payer to edit the note field"""

    required: Required[bool]
    """Requires to payer to fill the note field"""

    value: Required[Optional[str]]
    """Sets a note value to be preloaded in the checkout form"""


class Payer(TypedDict, total=False):
    document_number: Required[Optional[str]]
    """
    Sets the payer's document number, which will be preloaded into the checkout
    form. This field is alphanumeric, only accepts letters and numbers.
    """

    document_type: Required[
        Optional[Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]]
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

    email: Required[Optional[str]]
    """Sets the payer's email, which will be preloaded into the checkout form"""

    name: Required[Optional[str]]
    """Sets the payer's full name, which will be preloaded into the checkout form"""

    phone: Required[Optional[str]]
    """Sets the payer's phone number, which will be preloaded into the checkout form"""

    note: PayerNote
    """Sets the note field in the checkout form.

    When there is no note, and it is configured not to be editable, the checkout
    form's note field will not be visible.
    """


class Reference(TypedDict, total=False):
    editable: Required[bool]
    """Allows to payer to edit the reference field"""

    required: Required[bool]
    """Requires to payer to fill the reference field"""

    value: Required[Optional[str]]
    """Prefill the reference field into the form"""
