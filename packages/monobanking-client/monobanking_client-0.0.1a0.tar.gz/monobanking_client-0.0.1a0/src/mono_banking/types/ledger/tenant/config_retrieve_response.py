# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConfigRetrieveResponse", "CardConfigurationGroup"]


class CardConfigurationGroup(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    card_type: Optional[Literal["virtual", "plastic"]] = None

    country_code: Optional[str] = None
    """Country code of the card configuration"""

    name: Optional[str] = None
    """Name of the card configuration"""


class ConfigRetrieveResponse(BaseModel):
    card_configuration_groups: Optional[List[CardConfigurationGroup]] = None
    """
    Information about the customized card configurations specifically defined for
    the tenant.
    """

    self_account_holder_id: Optional[str] = None
    """Indicates the format for resource's ID"""

    supported_currencies: Optional[List[Literal["COP", "USD", "MXN"]]] = None
    """
    Denotes the configured currency codes that the tenant acknowledges within the
    Mono Ledger API environment.
    """
