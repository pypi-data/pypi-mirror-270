# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LookRetrieveResponse"]


class LookRetrieveResponse(BaseModel):
    card_id: Optional[str] = None
    """Card ID"""

    url: Optional[str] = None
    """URL using to embed the card information on web apps or sites using an iframe"""
