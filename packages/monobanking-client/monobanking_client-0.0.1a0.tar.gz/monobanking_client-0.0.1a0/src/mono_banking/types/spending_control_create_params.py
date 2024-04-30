# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SpendingControlCreateParams",
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


class SpendingControlCreateParams(TypedDict, total=False):
    currency_code: Required[Literal["COP", "USD", "MXN"]]
    """Spending control currency code"""

    rules: Required[Rules]
    """Configured spending control rules"""

    nickname: Optional[str]
    """Spending control nickname"""

    target: Literal["card"]
    """Spending control target"""


class RulesCardUsage(TypedDict, total=False):
    disabled_card_usages: Required[List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]]


class RulesVelocityDaily(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class RulesVelocityMonthly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class RulesVelocityWeekly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class RulesVelocity(TypedDict, total=False):
    daily: RulesVelocityDaily
    """Limit amount for daily spending"""

    monthly: RulesVelocityMonthly
    """Limit amount for monthly spending"""

    weekly: RulesVelocityWeekly
    """Limit amount for weekly spending"""


class RulesWithdrawalVelocityDaily(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class RulesWithdrawalVelocityMonthly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class RulesWithdrawalVelocity(TypedDict, total=False):
    daily: RulesWithdrawalVelocityDaily
    """Limit amount for daily withdrawal spending"""

    monthly: RulesWithdrawalVelocityMonthly
    """Limit amount for monthly withdrawal spending"""


class Rules(TypedDict, total=False):
    card_usage: RulesCardUsage

    velocity: RulesVelocity

    withdrawal_velocity: RulesWithdrawalVelocity
