# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RuleUpdateParams",
    "VelocitySchema",
    "VelocitySchemaDaily",
    "VelocitySchemaMonthly",
    "VelocitySchemaWeekly",
    "CardUsageSchema",
    "WithdrawalVelocitySchema",
    "WithdrawalVelocitySchemaDaily",
    "WithdrawalVelocitySchemaMonthly",
]


class VelocitySchema(TypedDict, total=False):
    type: Required[str]
    """String field"""

    daily: VelocitySchemaDaily
    """Limit amount for daily spending"""

    monthly: VelocitySchemaMonthly
    """Limit amount for monthly spending"""

    weekly: VelocitySchemaWeekly
    """Limit amount for weekly spending"""


class VelocitySchemaDaily(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class VelocitySchemaMonthly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class VelocitySchemaWeekly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class CardUsageSchema(TypedDict, total=False):
    disabled_card_usages: Required[List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]]

    type: Required[str]
    """String field"""


class WithdrawalVelocitySchema(TypedDict, total=False):
    type: Required[str]
    """String field"""

    daily: WithdrawalVelocitySchemaDaily
    """Limit amount for daily withdrawal spending"""

    monthly: WithdrawalVelocitySchemaMonthly
    """Limit amount for monthly withdrawal spending"""


class WithdrawalVelocitySchemaDaily(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


class WithdrawalVelocitySchemaMonthly(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""


RuleUpdateParams = Union[VelocitySchema, CardUsageSchema, WithdrawalVelocitySchema]
