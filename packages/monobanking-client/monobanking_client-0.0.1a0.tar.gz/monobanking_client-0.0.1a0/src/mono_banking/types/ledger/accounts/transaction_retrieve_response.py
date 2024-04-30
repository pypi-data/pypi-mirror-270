# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "TransactionRetrieveResponse",
    "CardTransactionOriginDetail",
    "CardTransactionOriginDetailAmount",
    "CardTransactionOriginDetailDetails",
    "CardTransactionOriginDetailDetailsAmount",
    "CardTransactionOriginDetailDetailsMerchantAmount",
    "SubaccountOperationOriginDetail",
    "SubaccountOperationOriginDetailAmount",
    "SubaccountOperationOriginDetailDetails",
    "SubaccountOperationOriginDetailDetailsAmount",
    "UnknownOrigin",
    "UnknownOriginAmount",
]


class CardTransactionOriginDetailAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class CardTransactionOriginDetailDetailsAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class CardTransactionOriginDetailDetailsMerchantAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class CardTransactionOriginDetailDetails(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[CardTransactionOriginDetailDetailsAmount] = None
    """Money schema"""

    card_id: Optional[str] = None
    """Indicates the format for resource's ID"""

    declination_reason: Optional[
        Literal[
            "account_blocked",
            "account_canceled",
            "account_holder_blocked",
            "account_holder_canceled",
            "card_daily_limit_exceeded",
            "card_weekly_limit_exceeded",
            "card_monthly_limit_exceeded",
            "daily_limit_exceeded",
            "monthly_limit_exceeded",
            "insufficient_funds",
            "insufficient_funds_gmf",
            "card_insufficient_funds",
            "card_insufficient_funds_gmf",
            "pending_transfers",
            "bank_connection_issue",
            "provider_no_request",
            "provider_timeout",
            "velocity_daily_exceeded",
            "velocity_weekly_exceeded",
            "velocity_monthly_exceeded",
            "withdrawal_velocity_daily_exceeded",
            "withdrawal_velocity_monthly_exceeded",
            "card_frozen",
            "card_canceled",
            "card_expired",
            "invalid_cvc",
            "invalid_exp_date",
            "invalid_pin",
            "pin_try_limit",
            "online_purchase_disabled",
            "physical_purchase_disabled",
            "atm_withdrawal_disabled",
            "other",
        ]
    ] = None
    """declination reason"""

    merchant_amount: Optional[CardTransactionOriginDetailDetailsMerchantAmount] = None
    """Money schema"""

    merchant_name: Optional[str] = None
    """String field"""

    state: Optional[
        Literal["created", "approved", "declined", "partially_captured", "fully_captured", "reversed"]
    ] = None
    """transaction state"""

    transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was made"""

    type: Optional[Literal["authorization", "authorization", "capture", "refund"]] = None
    """transaction type"""


class CardTransactionOriginDetail(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[CardTransactionOriginDetailAmount] = None
    """Money schema"""

    description: Optional[str] = None
    """useful infomation about the transaction"""

    details: Optional[CardTransactionOriginDetailDetails] = None

    id_in_origin: Optional[str] = None
    """String field"""

    operation_type: Optional[Literal["debit", "credit", "hold", "release"]] = None
    """The four common transaction operations are credit, debit, hold, and release:

    - credit: Increases the balance of the account. It is typically used to
      represent income.
    - debit: Decreases the balance of the account. It is typically used to represent
      expenses.
    - hold: Setting aside of funds for a specific purpose, such as a pending
      transaction.
    - release: Represent the release of previously held funds for a pending
      transaction.
    """

    origin: Optional[str] = None
    """The operation from which the transaction originated"""

    origin_transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was created"""

    reverted_by_id: Optional[str] = None
    """The ID of the transaction that reverts this ledger transaction"""

    reverts_id: Optional[str] = None
    """The ID of the transaction that this ledger transaction reverts"""

    transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was actually performed"""


class SubaccountOperationOriginDetailAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SubaccountOperationOriginDetailDetailsAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class SubaccountOperationOriginDetailDetails(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[SubaccountOperationOriginDetailDetailsAmount] = None
    """Money schema"""

    description: Optional[str] = None
    """String field"""

    destination_account_id: Optional[str] = None
    """Indicates the format for resource's ID"""

    external_id: Optional[str] = None
    """String field"""

    operation_type: Optional[Literal["topup", "withdrawal", "account_to_account"]] = None
    """operation type"""

    origin_account_id: Optional[str] = None
    """Indicates the format for resource's ID"""

    reference: Optional[str] = None
    """String field"""

    state: Optional[Literal["created", "successful", "rejected"]] = None
    """operation state"""

    state_reasons: Optional[Literal["insufficient_funds", "unknown"]] = None
    """reason of the operation state"""


class SubaccountOperationOriginDetail(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[SubaccountOperationOriginDetailAmount] = None
    """Money schema"""

    description: Optional[str] = None
    """useful infomation about the transaction"""

    details: Optional[SubaccountOperationOriginDetailDetails] = None

    id_in_origin: Optional[str] = None
    """String field"""

    operation_type: Optional[Literal["debit", "credit", "hold", "release"]] = None
    """The four common transaction operations are credit, debit, hold, and release:

    - credit: Increases the balance of the account. It is typically used to
      represent income.
    - debit: Decreases the balance of the account. It is typically used to represent
      expenses.
    - hold: Setting aside of funds for a specific purpose, such as a pending
      transaction.
    - release: Represent the release of previously held funds for a pending
      transaction.
    """

    origin: Optional[str] = None
    """The operation from which the transaction originated"""

    origin_transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was created"""

    reverted_by_id: Optional[str] = None
    """The ID of the transaction that reverts this ledger transaction"""

    reverts_id: Optional[str] = None
    """The ID of the transaction that this ledger transaction reverts"""

    transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was actually performed"""


class UnknownOriginAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class UnknownOrigin(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[UnknownOriginAmount] = None
    """Money schema"""

    description: Optional[str] = None
    """useful infomation about the transaction"""

    details: Optional[object] = None

    id_in_origin: Optional[str] = None
    """String field"""

    operation_type: Optional[Literal["debit", "credit", "hold", "release"]] = None
    """The four common transaction operations are credit, debit, hold, and release:

    - credit: Increases the balance of the account. It is typically used to
      represent income.
    - debit: Decreases the balance of the account. It is typically used to represent
      expenses.
    - hold: Setting aside of funds for a specific purpose, such as a pending
      transaction.
    - release: Represent the release of previously held funds for a pending
      transaction.
    """

    origin: Optional[str] = None
    """The operation from which the transaction originated"""

    origin_transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was created"""

    reverted_by_id: Optional[str] = None
    """The ID of the transaction that reverts this ledger transaction"""

    reverts_id: Optional[str] = None
    """The ID of the transaction that this ledger transaction reverts"""

    transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was actually performed"""


TransactionRetrieveResponse = Union[CardTransactionOriginDetail, SubaccountOperationOriginDetail, UnknownOrigin]
