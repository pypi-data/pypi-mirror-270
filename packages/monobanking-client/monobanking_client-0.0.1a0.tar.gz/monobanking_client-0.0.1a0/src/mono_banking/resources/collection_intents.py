# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import collection_intent_list_params, collection_intent_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.collection_intent_list_response import CollectionIntentListResponse
from ..types.collection_intent_create_response import CollectionIntentCreateResponse
from ..types.collection_intent_retrieve_response import CollectionIntentRetrieveResponse

__all__ = ["CollectionIntentsResource", "AsyncCollectionIntentsResource"]


class CollectionIntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionIntentsResourceWithRawResponse:
        return CollectionIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionIntentsResourceWithStreamingResponse:
        return CollectionIntentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: collection_intent_create_params.Amount,
        bank_code: str,
        ip: str,
        payer: collection_intent_create_params.Payer,
        payment: collection_intent_create_params.Payment,
        redirect_url: str,
        note: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionIntentCreateResponse:
        """
        You can use this endpoint to create a collection intent

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          bank_code: Bank code used by PSE to make the collection

          ip: The user IP address

          redirect_url: The URL to redirect when the collection intent successfully completes through
              the provider.

          note: Note indicated by the user of the client

          reference: Reference indicated by the client or by the user of the client

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/collection_intents",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "bank_code": bank_code,
                    "ip": ip,
                    "payer": payer,
                    "payment": payment,
                    "redirect_url": redirect_url,
                    "note": note,
                    "reference": reference,
                },
                collection_intent_create_params.CollectionIntentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionIntentCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionIntentRetrieveResponse:
        """
        Get collection intent detail

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/collection_intents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionIntentRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        collection_link_id: str | NotGiven = NOT_GIVEN,
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
    ) -> CollectionIntentListResponse:
        """
        This endpoint allows you to list your collection intents, optionally filtered by
        state, account. and collection link id

        Args:
          account_id: Account ID (Base 62 format)

          collection_link_id: Collection link ID (Base 62 format)

          page_number: Page number

          page_size: Page size

          state: State of the collection intents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/collection_intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "collection_link_id": collection_link_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                    },
                    collection_intent_list_params.CollectionIntentListParams,
                ),
            ),
            cast_to=CollectionIntentListResponse,
        )


class AsyncCollectionIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionIntentsResourceWithRawResponse:
        return AsyncCollectionIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionIntentsResourceWithStreamingResponse:
        return AsyncCollectionIntentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: collection_intent_create_params.Amount,
        bank_code: str,
        ip: str,
        payer: collection_intent_create_params.Payer,
        payment: collection_intent_create_params.Payment,
        redirect_url: str,
        note: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionIntentCreateResponse:
        """
        You can use this endpoint to create a collection intent

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          bank_code: Bank code used by PSE to make the collection

          ip: The user IP address

          redirect_url: The URL to redirect when the collection intent successfully completes through
              the provider.

          note: Note indicated by the user of the client

          reference: Reference indicated by the client or by the user of the client

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/collection_intents",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "bank_code": bank_code,
                    "ip": ip,
                    "payer": payer,
                    "payment": payment,
                    "redirect_url": redirect_url,
                    "note": note,
                    "reference": reference,
                },
                collection_intent_create_params.CollectionIntentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionIntentCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionIntentRetrieveResponse:
        """
        Get collection intent detail

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/collection_intents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionIntentRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        collection_link_id: str | NotGiven = NOT_GIVEN,
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
    ) -> CollectionIntentListResponse:
        """
        This endpoint allows you to list your collection intents, optionally filtered by
        state, account. and collection link id

        Args:
          account_id: Account ID (Base 62 format)

          collection_link_id: Collection link ID (Base 62 format)

          page_number: Page number

          page_size: Page size

          state: State of the collection intents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/collection_intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "collection_link_id": collection_link_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                    },
                    collection_intent_list_params.CollectionIntentListParams,
                ),
            ),
            cast_to=CollectionIntentListResponse,
        )


class CollectionIntentsResourceWithRawResponse:
    def __init__(self, collection_intents: CollectionIntentsResource) -> None:
        self._collection_intents = collection_intents

        self.create = to_raw_response_wrapper(
            collection_intents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collection_intents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collection_intents.list,
        )


class AsyncCollectionIntentsResourceWithRawResponse:
    def __init__(self, collection_intents: AsyncCollectionIntentsResource) -> None:
        self._collection_intents = collection_intents

        self.create = async_to_raw_response_wrapper(
            collection_intents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collection_intents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collection_intents.list,
        )


class CollectionIntentsResourceWithStreamingResponse:
    def __init__(self, collection_intents: CollectionIntentsResource) -> None:
        self._collection_intents = collection_intents

        self.create = to_streamed_response_wrapper(
            collection_intents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collection_intents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collection_intents.list,
        )


class AsyncCollectionIntentsResourceWithStreamingResponse:
    def __init__(self, collection_intents: AsyncCollectionIntentsResource) -> None:
        self._collection_intents = collection_intents

        self.create = async_to_streamed_response_wrapper(
            collection_intents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collection_intents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collection_intents.list,
        )
