# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.collection_links import intent_list_params
from ...types.collection_links.intent_list_response import IntentListResponse
from ...types.collection_links.intent_retrieve_response import IntentRetrieveResponse

__all__ = ["IntentsResource", "AsyncIntentsResource"]


class IntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntentsResourceWithRawResponse:
        return IntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntentsResourceWithStreamingResponse:
        return IntentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        collection_link_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntentRetrieveResponse:
        """
        Get collection intent detail

        Args:
          collection_link_id: Indicates the format for resource's ID

          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_link_id:
            raise ValueError(f"Expected a non-empty value for `collection_link_id` but received {collection_link_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/collection_links/{collection_link_id}/intents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntentRetrieveResponse,
        )

    def list(
        self,
        collection_link_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Literal["all", "created", "in_progress", "approved_in_provider", "account_credited", "failed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntentListResponse:
        """
        This endpoint allows you to list the successful collection intents

        Args:
          collection_link_id: Indicates the format for resource's ID

          page_number: Page number

          page_size: Page size

          state: State of the collection intents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_link_id:
            raise ValueError(f"Expected a non-empty value for `collection_link_id` but received {collection_link_id!r}")
        return self._get(
            f"/v1/collection_links/{collection_link_id}/intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                    },
                    intent_list_params.IntentListParams,
                ),
            ),
            cast_to=IntentListResponse,
        )


class AsyncIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntentsResourceWithRawResponse:
        return AsyncIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntentsResourceWithStreamingResponse:
        return AsyncIntentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        collection_link_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntentRetrieveResponse:
        """
        Get collection intent detail

        Args:
          collection_link_id: Indicates the format for resource's ID

          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_link_id:
            raise ValueError(f"Expected a non-empty value for `collection_link_id` but received {collection_link_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/collection_links/{collection_link_id}/intents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntentRetrieveResponse,
        )

    async def list(
        self,
        collection_link_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Literal["all", "created", "in_progress", "approved_in_provider", "account_credited", "failed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntentListResponse:
        """
        This endpoint allows you to list the successful collection intents

        Args:
          collection_link_id: Indicates the format for resource's ID

          page_number: Page number

          page_size: Page size

          state: State of the collection intents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_link_id:
            raise ValueError(f"Expected a non-empty value for `collection_link_id` but received {collection_link_id!r}")
        return await self._get(
            f"/v1/collection_links/{collection_link_id}/intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                    },
                    intent_list_params.IntentListParams,
                ),
            ),
            cast_to=IntentListResponse,
        )


class IntentsResourceWithRawResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.retrieve = to_raw_response_wrapper(
            intents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            intents.list,
        )


class AsyncIntentsResourceWithRawResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.retrieve = async_to_raw_response_wrapper(
            intents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            intents.list,
        )


class IntentsResourceWithStreamingResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.retrieve = to_streamed_response_wrapper(
            intents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            intents.list,
        )


class AsyncIntentsResourceWithStreamingResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.retrieve = async_to_streamed_response_wrapper(
            intents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            intents.list,
        )
