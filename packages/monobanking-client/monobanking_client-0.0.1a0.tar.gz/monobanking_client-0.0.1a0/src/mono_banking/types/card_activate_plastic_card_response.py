# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CardActivatePlasticCardResponse"]


class CardActivatePlasticCardResponse(BaseModel):
    url: str
    """Contains the plastic card activation link URL"""

    id: Optional[str] = None
    """Plastic Card Activation ID"""
