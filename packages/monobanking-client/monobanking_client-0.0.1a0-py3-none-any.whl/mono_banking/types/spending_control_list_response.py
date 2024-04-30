# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SpendingControlListResponse",
    "Pagination",
    "SpendingControl",
    "SpendingControlRules",
    "SpendingControlRulesCardUsage",
    "SpendingControlRulesVelocity",
    "SpendingControlRulesVelocityDaily",
    "SpendingControlRulesVelocityMonthly",
    "SpendingControlRulesVelocityWeekly",
    "SpendingControlRulesWithdrawalVelocity",
    "SpendingControlRulesWithdrawalVelocityDaily",
    "SpendingControlRulesWithdrawalVelocityMonthly",
]


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class SpendingControlRulesCardUsage(BaseModel):
    disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]


class SpendingControlRulesVelocityDaily(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SpendingControlRulesVelocityMonthly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SpendingControlRulesVelocityWeekly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SpendingControlRulesVelocity(BaseModel):
    daily: Optional[SpendingControlRulesVelocityDaily] = None
    """Limit amount for daily spending"""

    monthly: Optional[SpendingControlRulesVelocityMonthly] = None
    """Limit amount for monthly spending"""

    weekly: Optional[SpendingControlRulesVelocityWeekly] = None
    """Limit amount for weekly spending"""


class SpendingControlRulesWithdrawalVelocityDaily(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SpendingControlRulesWithdrawalVelocityMonthly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class SpendingControlRulesWithdrawalVelocity(BaseModel):
    daily: Optional[SpendingControlRulesWithdrawalVelocityDaily] = None
    """Limit amount for daily withdrawal spending"""

    monthly: Optional[SpendingControlRulesWithdrawalVelocityMonthly] = None
    """Limit amount for monthly withdrawal spending"""


class SpendingControlRules(BaseModel):
    card_usage: Optional[SpendingControlRulesCardUsage] = None

    velocity: Optional[SpendingControlRulesVelocity] = None

    withdrawal_velocity: Optional[SpendingControlRulesWithdrawalVelocity] = None


class SpendingControl(BaseModel):
    currency_code: Literal["COP", "USD", "MXN"]
    """Spending control currency code"""

    rules: SpendingControlRules
    """Configured spending control rules"""

    id: Optional[str] = None
    """Spending Control ID"""

    nickname: Optional[str] = None
    """Spending control nickname"""

    target: Optional[Literal["card"]] = None
    """Spending control target"""


class SpendingControlListResponse(BaseModel):
    pagination: Optional[Pagination] = None
    """Pagination schema"""

    spending_controls: Optional[List[SpendingControl]] = None
    """It contains a list with spending controls"""
