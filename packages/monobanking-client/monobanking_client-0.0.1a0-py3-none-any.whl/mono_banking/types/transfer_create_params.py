# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransferCreateParams", "Transfer", "TransferAmount", "TransferPayee", "TransferPayeeBankAccount"]


class TransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """
    Represents the account of the client to which a debit entry will be made as a
    result of the transaction.
    """

    transfers: Required[Iterable[Transfer]]
    """It contains a list with transfers"""


class TransferAmount(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP"]]
    """Currency of money"""


class TransferPayeeBankAccount(TypedDict, total=False):
    bank_code: Required[str]
    """
    Sets the bank code, which is used to identify the bank where the money will be
    transferred.

    You can find the bank code by using the GET banks endpoint and look the code
    field.
    """

    number: Required[str]
    """Sets the payee's account number"""

    type: Required[Literal["savings_account", "checking_account", "electronic_deposit"]]
    """Sets the payee's account type"""


class TransferPayee(TypedDict, total=False):
    bank_account: Required[TransferPayeeBankAccount]
    """
    Sets the destination bank account information, which will be contain the bank,
    account type and the account number to be transferred the money.
    """

    document_number: Required[str]
    """Sets the payee's document number"""

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

    name: Required[str]
    """Sets the payee's full name"""

    email: Optional[str]
    """Sets the payee's email"""

    phone_number: Optional[str]
    """Sets the payee's phone number"""


class Transfer(TypedDict, total=False):
    amount: Required[TransferAmount]
    """Represents the amount of money to make the bank transfer"""

    entity_id: Required[str]
    """Represents a unique transfer id generated and provided by the API user.

    The API user is responsible to generate and provide a unique id for all their
    organization's transfers. New transfers with a previously registered entity_id
    are going to be logged as duplicated. Duplicated transfers don't participate in
    any money movement. Transfers generated through mono's web application don't
    have an entity_id.
    """

    payee: Required[TransferPayee]
    """
    Sets the payee data, which will be used to specify the details about the
    destination bank account
    """

    description: Optional[str]
    """Sets the description of the transfer"""

    emails_to_notify: Optional[List[Optional[str]]]
    """
    It contains a list with the emails that will receive the receipt of the bank
    transfer
    """

    fallback_routing: List[Literal["ach"]]
    """This field is used to specify a fallback routing option for bank transfers:

    - `ach`: This option sends the bank transfer through the ACH network if the
      initial attempt using the `turbo` routing option fails.

    Use case:

    if the `routing` field is `turbo` and `fallback_routing` is `["ach"]`, which
    means that the bank transfer will be sent in real-time. However, if the initial
    attempt to send the transfer using the `turbo` option fails, the transfer will
    be sent through the ACH.

    This field will only be used if the initial attempt to send the transfer using
    the `turbo` option fails. If the initial attempt succeeds, no fallback routing
    option will be used.
    """

    reference: Optional[str]
    """Sets the reference of the transfer"""

    routing: Literal["ach", "turbo"]
    """Represents where the bank transfers will be processed:

    - `ach`: This option sends the bank transfer through the ACH network. ACH is a
      batch processing system that is used to transfer funds between banks. This
      option takes 1 or 2 days to complete.
    - `turbo`: This option sends the bank transfer in real-time. It's important to
      note that it is only available to certain banks. You can check the supported
      banks by making a GET request to the `/banks` endpoint.
    """
