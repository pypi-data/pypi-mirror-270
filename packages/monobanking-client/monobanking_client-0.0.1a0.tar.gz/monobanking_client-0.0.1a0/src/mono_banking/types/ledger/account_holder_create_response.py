# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountHolderCreateResponse", "Address", "Person"]


class Address(BaseModel):
    city: str
    """City, district, suburb, town, or village"""

    country: str
    """Country code ISO 3166-1 alpha-2"""

    line_1: str
    """Street, P.O. Box, or address information"""

    state: str
    """State, province, region, or county"""

    zip_code: str

    extra: Optional[str] = None
    """Additional information"""

    line_2: Optional[str] = None
    """Home, apartment, room, suite, office, or building"""


class Person(BaseModel):
    country_code: str
    """
    Country code related to the person, this field use the ISO 3166-1 alpha-2 and
    alpha-3 standards.
    """

    document_number: str
    """String field"""

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

    first_name: str

    last_name: str

    person_type: Literal["natural", "legal"]
    """Denotes if the person is a natural or a legal entity"""

    middle_name: Optional[str] = None

    second_last_name: Optional[str] = None


class AccountHolderCreateResponse(BaseModel):
    address: Address
    """Contains the address information related to the account holder."""

    external_id: Optional[str] = None
    """Represents a unique external_id generated and provided by the API user.

    The API user is responsible to generate and provide a unique id for all their
    organization's account holders.
    """

    person: Person
    """Contains the specific person information of the account holder."""

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    client_id: Optional[str] = None
    """Identifier of the clientID, this property is only a read-only field"""

    email: Optional[str] = None
    """Account holder's email"""

    inserted_at: Optional[datetime] = None
    """Indicates when an account holder was created"""

    metadata: Optional[object] = None
    """
    Contains additional information that provide context, description, or
    supplementary details about the data being transmitted.
    """

    phone_number: Optional[str] = None
    """Account holder's phone number"""

    state: Optional[Literal["active", "blocked", "canceled"]] = None
    """
    It represents the current state of the account holder, and these are the
    possible states of an account holder:

    - active: it is enable to manage and perform actions with its accounts.
    - blocked: it is blocked by the tenant, but you could also make it active again.
    - canceled: it is canceled by Mono directly and can't use their accounts
      anymore.
    """

    state_reason: Optional[Literal["fraud", "user_request", "other"]] = None
    """It provides the reason why the account holder could be blocked or canceled.

    It is required when the account holder is transitioned to being blocked or
    canceled.
    """

    state_reason_detail: Optional[str] = None
    """
    It provides a textual reason why the account holder is blocked or canceled in
    case of the state_reason value is `other`.
    """

    type: Optional[Literal["self", "third_party"]] = None
    """Account holders can be one of the following types:

    - self: the "self" account holder refers to the tenant interacting directly with
      the API.
    - third_party: The "third_party" account holder represents a client associated
      with the tenant. In this scenario, the tenant acts as an intermediary managing
      the account on behalf of their own client.

    For our API, you can only create third-party account holders, self account
    holder is only for internal use.
    """

    updated_at: Optional[datetime] = None
    """Indicates when an account holder was updated"""
