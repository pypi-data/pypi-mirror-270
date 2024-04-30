# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "TransferCreateResponse",
    "Transfer",
    "TransferAmount",
    "TransferPayee",
    "TransferPayeeBankAccount",
    "TransferBatch",
    "TransferBatchTotalAmount",
]


class TransferAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class TransferPayeeBankAccount(BaseModel):
    bank_code: str
    """
    Sets the bank code, which is used to identify the bank where the money will be
    transferred.

    You can find the bank code by using the GET banks endpoint and look the code
    field.
    """

    number: str
    """Sets the payee's account number"""

    type: Literal["savings_account", "checking_account", "electronic_deposit"]
    """Sets the payee's account type"""


class TransferPayee(BaseModel):
    bank_account: TransferPayeeBankAccount
    """
    Sets the destination bank account information, which will be contain the bank,
    account type and the account number to be transferred the money.
    """

    document_number: str
    """Sets the payee's document number"""

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
    """Sets the payee's full name"""

    email: Optional[str] = None
    """Sets the payee's email"""

    phone_number: Optional[str] = None
    """Sets the payee's phone number"""


class TransferBatchTotalAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class TransferBatch(BaseModel):
    account_id: str
    """
    Represents the account of the client to which a debit entry will be made as a
    result of the transaction.
    """

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    inserted_at: Optional[datetime] = None
    """Indicates when a batch of transfers was created"""

    origin: Optional[Literal["file", "manual", "api"]] = None
    """Represents the creation origin of the transfer's batch.

    - file: When transfers were uploaded by an excel file.
    - manual: When transfers were created into the Mono Dashboard.
    - api: When transfers were uploaded through Mono Banking API.
    """

    state: Optional[
        Literal[
            "created",
            "pending_otp",
            "verified_otp",
            "cancelled",
            "processing_transactions",
            "partially_approved",
            "declined",
            "approved",
            "duplicated",
        ]
    ] = None
    """Represents the batch state"""

    total_amount: Optional[TransferBatchTotalAmount] = None
    """Represents the total amount of money of the batch."""

    updated_at: Optional[datetime] = None
    """Indicates when a batch of transfers was updated"""


class Transfer(BaseModel):
    amount: TransferAmount
    """Represents the amount of money to make the bank transfer"""

    entity_id: str
    """Represents a unique transfer id generated and provided by the API user.

    The API user is responsible to generate and provide a unique id for all their
    organization's transfers. New transfers with a previously registered entity_id
    are going to be logged as duplicated. Duplicated transfers don't participate in
    any money movement. Transfers generated through mono's web application don't
    have an entity_id.
    """

    payee: TransferPayee
    """
    Sets the payee data, which will be used to specify the details about the
    destination bank account
    """

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    batch: Optional[TransferBatch] = None
    """A batch of transfers represents a group of transfers data."""

    declination_reason: Optional[
        Literal[
            "account_closed",
            "account_inactive_or_blocked",
            "account_not_found",
            "account_not_opened",
            "account_type_mismatch",
            "authorization_revoked",
            "daily_amount_limit_exceeded",
            "daily_count_limit_exceeded",
            "debit_transaction_contingency_return",
            "definition_product",
            "delegate_dead",
            "destination_signer_not_found",
            "disabled_account",
            "electronic_deposit_account",
            "funds_unavailable",
            "global_limit_exceeded",
            "id_does_not_match",
            "insufficient_funds",
            "invalid_account",
            "invalid_effective_date",
            "invalid_payee_account_data",
            "monthly_amount_limit_exceeded",
            "monthly_count_limit_exceeded",
            "order_no_payment",
            "payee_dead",
            "payee_electronic_deposit_not_enabled",
            "payee_requested_return",
            "payee_return_credit_transaction",
            "payee_return_debit_transaction",
            "payer_not_authorized",
            "prenotification_does_not_exist",
            "prenotification_not_processed_by_receiving_entity",
            "return_request_efo",
            "seizure_account",
            "target_rejected_transfer",
            "transaction_deadline_exceeded",
            "unknown",
            "user_abandoned_transaction_in_bank",
        ]
    ] = None
    """
    Returns the reason why the bank transfer couldn't be approved by the destination
    bank.
    """

    description: Optional[str] = None
    """Sets the description of the transfer"""

    emails_to_notify: Optional[List[Optional[str]]] = None
    """
    It contains a list with the emails that will receive the receipt of the bank
    transfer
    """

    fallback_routing: Optional[List[Literal["ach"]]] = None
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

    inserted_at: Optional[datetime] = None
    """Indicates when a transfer was created"""

    reference: Optional[str] = None
    """Sets the reference of the transfer"""

    routing: Optional[Literal["ach", "turbo"]] = None
    """Represents where the bank transfers will be processed:

    - `ach`: This option sends the bank transfer through the ACH network. ACH is a
      batch processing system that is used to transfer funds between banks. This
      option takes 1 or 2 days to complete.
    - `turbo`: This option sends the bank transfer in real-time. It's important to
      note that it is only available to certain banks. You can check the supported
      banks by making a GET request to the `/banks` endpoint.
    """

    state: Optional[Literal["created", "in_progress", "cancelled", "declined", "approved", "duplicated"]] = None
    """Represents the current transfer state, it can have the following states:

    - created: Indicates that the bank transfer has been created in our system, but
      it has not yet been sent to the bank for processing.
    - in_progress: Indicates that the bank transfer is currently being processed by
      the bank. This includes steps such as verifying the account information,
      transferring the funds between accounts, and updating the account balances.
      This state occurs when the bank is working on executing the bank transfer, but
      it has not yet been completed.
    - approved: Indicates that the bank transfer has been approved by the bank and
      has been successfully executed. This means that the funds have been
      transferred from the source account to the destination account, and the
      account balances have been updated accordingly.
    - declined: Indicates that the bank transfer has been rejected by the bank and
      will not be executed. This may occur due to a variety of reasons, such as
      insufficient funds in the source account, invalid account information, or
      regulatory restrictions.
    - cancelled: Indicates that the bank transfer has been canceled by a user. This
      occurs if the client decides to cancel the transfer before it has been sent to
      the bank.
    - duplicated: Indicates that the bank transfer has already been received in our
      system, and the repeated record will not be taken into account. This could be
      because the transfer was sent multiple times with the same "entity_id" field.
    """

    updated_at: Optional[datetime] = None
    """Indicates when a transfer was updated"""


class TransferCreateResponse(BaseModel):
    transfers: List[Transfer]
    """It contains a list with transfers"""
