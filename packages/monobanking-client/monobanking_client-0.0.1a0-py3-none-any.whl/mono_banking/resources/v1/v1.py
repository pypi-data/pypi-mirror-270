# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cards import (
    CardsResource,
    AsyncCardsResource,
    CardsResourceWithRawResponse,
    AsyncCardsResourceWithRawResponse,
    CardsResourceWithStreamingResponse,
    AsyncCardsResourceWithStreamingResponse,
)
from .ledger import (
    LedgerResource,
    AsyncLedgerResource,
    LedgerResourceWithRawResponse,
    AsyncLedgerResourceWithRawResponse,
    LedgerResourceWithStreamingResponse,
    AsyncLedgerResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .cards.cards import CardsResource, AsyncCardsResource
from .ledger.ledger import LedgerResource, AsyncLedgerResource
from .collection_links import (
    CollectionLinksResource,
    AsyncCollectionLinksResource,
    CollectionLinksResourceWithRawResponse,
    AsyncCollectionLinksResourceWithRawResponse,
    CollectionLinksResourceWithStreamingResponse,
    AsyncCollectionLinksResourceWithStreamingResponse,
)
from .spending_controls import (
    SpendingControlsResource,
    AsyncSpendingControlsResource,
    SpendingControlsResourceWithRawResponse,
    AsyncSpendingControlsResourceWithRawResponse,
    SpendingControlsResourceWithStreamingResponse,
    AsyncSpendingControlsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def spending_controls(self) -> SpendingControlsResource:
        return SpendingControlsResource(self._client)

    @cached_property
    def ledger(self) -> LedgerResource:
        return LedgerResource(self._client)

    @cached_property
    def collection_links(self) -> CollectionLinksResource:
        return CollectionLinksResource(self._client)

    @cached_property
    def cards(self) -> CardsResource:
        return CardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def spending_controls(self) -> AsyncSpendingControlsResource:
        return AsyncSpendingControlsResource(self._client)

    @cached_property
    def ledger(self) -> AsyncLedgerResource:
        return AsyncLedgerResource(self._client)

    @cached_property
    def collection_links(self) -> AsyncCollectionLinksResource:
        return AsyncCollectionLinksResource(self._client)

    @cached_property
    def cards(self) -> AsyncCardsResource:
        return AsyncCardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def spending_controls(self) -> SpendingControlsResourceWithRawResponse:
        return SpendingControlsResourceWithRawResponse(self._v1.spending_controls)

    @cached_property
    def ledger(self) -> LedgerResourceWithRawResponse:
        return LedgerResourceWithRawResponse(self._v1.ledger)

    @cached_property
    def collection_links(self) -> CollectionLinksResourceWithRawResponse:
        return CollectionLinksResourceWithRawResponse(self._v1.collection_links)

    @cached_property
    def cards(self) -> CardsResourceWithRawResponse:
        return CardsResourceWithRawResponse(self._v1.cards)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def spending_controls(self) -> AsyncSpendingControlsResourceWithRawResponse:
        return AsyncSpendingControlsResourceWithRawResponse(self._v1.spending_controls)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithRawResponse:
        return AsyncLedgerResourceWithRawResponse(self._v1.ledger)

    @cached_property
    def collection_links(self) -> AsyncCollectionLinksResourceWithRawResponse:
        return AsyncCollectionLinksResourceWithRawResponse(self._v1.collection_links)

    @cached_property
    def cards(self) -> AsyncCardsResourceWithRawResponse:
        return AsyncCardsResourceWithRawResponse(self._v1.cards)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def spending_controls(self) -> SpendingControlsResourceWithStreamingResponse:
        return SpendingControlsResourceWithStreamingResponse(self._v1.spending_controls)

    @cached_property
    def ledger(self) -> LedgerResourceWithStreamingResponse:
        return LedgerResourceWithStreamingResponse(self._v1.ledger)

    @cached_property
    def collection_links(self) -> CollectionLinksResourceWithStreamingResponse:
        return CollectionLinksResourceWithStreamingResponse(self._v1.collection_links)

    @cached_property
    def cards(self) -> CardsResourceWithStreamingResponse:
        return CardsResourceWithStreamingResponse(self._v1.cards)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def spending_controls(self) -> AsyncSpendingControlsResourceWithStreamingResponse:
        return AsyncSpendingControlsResourceWithStreamingResponse(self._v1.spending_controls)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithStreamingResponse:
        return AsyncLedgerResourceWithStreamingResponse(self._v1.ledger)

    @cached_property
    def collection_links(self) -> AsyncCollectionLinksResourceWithStreamingResponse:
        return AsyncCollectionLinksResourceWithStreamingResponse(self._v1.collection_links)

    @cached_property
    def cards(self) -> AsyncCardsResourceWithStreamingResponse:
        return AsyncCardsResourceWithStreamingResponse(self._v1.cards)
