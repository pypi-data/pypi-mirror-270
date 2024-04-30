# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SpendingControlCreateResponse",
    "Rules",
    "RulesCardUsage",
    "RulesVelocity",
    "RulesVelocityDaily",
    "RulesVelocityMonthly",
    "RulesVelocityWeekly",
    "RulesWithdrawalVelocity",
    "RulesWithdrawalVelocityDaily",
    "RulesWithdrawalVelocityMonthly",
]


class RulesCardUsage(BaseModel):
    disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]


class RulesVelocityDaily(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class RulesVelocityMonthly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class RulesVelocityWeekly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class RulesVelocity(BaseModel):
    daily: Optional[RulesVelocityDaily] = None
    """Limit amount for daily spending"""

    monthly: Optional[RulesVelocityMonthly] = None
    """Limit amount for monthly spending"""

    weekly: Optional[RulesVelocityWeekly] = None
    """Limit amount for weekly spending"""


class RulesWithdrawalVelocityDaily(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class RulesWithdrawalVelocityMonthly(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class RulesWithdrawalVelocity(BaseModel):
    daily: Optional[RulesWithdrawalVelocityDaily] = None
    """Limit amount for daily withdrawal spending"""

    monthly: Optional[RulesWithdrawalVelocityMonthly] = None
    """Limit amount for monthly withdrawal spending"""


class Rules(BaseModel):
    card_usage: Optional[RulesCardUsage] = None

    velocity: Optional[RulesVelocity] = None

    withdrawal_velocity: Optional[RulesWithdrawalVelocity] = None


class SpendingControlCreateResponse(BaseModel):
    currency_code: Literal["COP", "USD", "MXN"]
    """Spending control currency code"""

    rules: Rules
    """Configured spending control rules"""

    id: Optional[str] = None
    """Spending Control ID"""

    nickname: Optional[str] = None
    """Spending control nickname"""

    target: Optional[Literal["card"]] = None
    """Spending control target"""
