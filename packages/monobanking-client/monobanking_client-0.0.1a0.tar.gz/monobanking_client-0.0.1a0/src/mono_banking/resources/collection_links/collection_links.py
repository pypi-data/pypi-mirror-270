# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .intents import (
    IntentsResource,
    AsyncIntentsResource,
    IntentsResourceWithRawResponse,
    AsyncIntentsResourceWithRawResponse,
    IntentsResourceWithStreamingResponse,
    AsyncIntentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CollectionLinksResource", "AsyncCollectionLinksResource"]


class CollectionLinksResource(SyncAPIResource):
    @cached_property
    def intents(self) -> IntentsResource:
        return IntentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionLinksResourceWithRawResponse:
        return CollectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionLinksResourceWithStreamingResponse:
        return CollectionLinksResourceWithStreamingResponse(self)


class AsyncCollectionLinksResource(AsyncAPIResource):
    @cached_property
    def intents(self) -> AsyncIntentsResource:
        return AsyncIntentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionLinksResourceWithRawResponse:
        return AsyncCollectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionLinksResourceWithStreamingResponse:
        return AsyncCollectionLinksResourceWithStreamingResponse(self)


class CollectionLinksResourceWithRawResponse:
    def __init__(self, collection_links: CollectionLinksResource) -> None:
        self._collection_links = collection_links

    @cached_property
    def intents(self) -> IntentsResourceWithRawResponse:
        return IntentsResourceWithRawResponse(self._collection_links.intents)


class AsyncCollectionLinksResourceWithRawResponse:
    def __init__(self, collection_links: AsyncCollectionLinksResource) -> None:
        self._collection_links = collection_links

    @cached_property
    def intents(self) -> AsyncIntentsResourceWithRawResponse:
        return AsyncIntentsResourceWithRawResponse(self._collection_links.intents)


class CollectionLinksResourceWithStreamingResponse:
    def __init__(self, collection_links: CollectionLinksResource) -> None:
        self._collection_links = collection_links

    @cached_property
    def intents(self) -> IntentsResourceWithStreamingResponse:
        return IntentsResourceWithStreamingResponse(self._collection_links.intents)


class AsyncCollectionLinksResourceWithStreamingResponse:
    def __init__(self, collection_links: AsyncCollectionLinksResource) -> None:
        self._collection_links = collection_links

    @cached_property
    def intents(self) -> AsyncIntentsResourceWithStreamingResponse:
        return AsyncIntentsResourceWithStreamingResponse(self._collection_links.intents)
