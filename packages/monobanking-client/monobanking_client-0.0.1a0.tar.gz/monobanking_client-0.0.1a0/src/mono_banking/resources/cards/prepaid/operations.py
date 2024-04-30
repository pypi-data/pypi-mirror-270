# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.cards.prepaid import operation_create_params, operation_retrieve_params
from ....types.cards.prepaid.operation_retrieve_response import OperationRetrieveResponse

__all__ = ["OperationsResource", "AsyncOperationsResource"]


class OperationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self)

    def create(
        self,
        card_id: str,
        *,
        amount: operation_create_params.Amount,
        operation: Literal["topup", "withdrawal"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Topping up and withdrawing the card balance

        Args:
          card_id: Indicates the format for resource's ID

          amount: deposit balance amount

          operation:
              there are two operation types:

              - topup: Increments the card balance.
              - withdrawal: Reduces the card balance.

          description: String field

          entity_id: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/cards/{card_id}/prepaid/operations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "operation": operation,
                    "description": description,
                    "entity_id": entity_id,
                },
                operation_create_params.OperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        performed_at: operation_retrieve_params.PerformedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationRetrieveResponse:
        """
        Gets card balance operations

        Args:
          card_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          performed_at: Filters the operations by performed date and time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/v1/cards/{card_id}/prepaid/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "performed_at": performed_at,
                    },
                    operation_retrieve_params.OperationRetrieveParams,
                ),
            ),
            cast_to=OperationRetrieveResponse,
        )


class AsyncOperationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self)

    async def create(
        self,
        card_id: str,
        *,
        amount: operation_create_params.Amount,
        operation: Literal["topup", "withdrawal"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Topping up and withdrawing the card balance

        Args:
          card_id: Indicates the format for resource's ID

          amount: deposit balance amount

          operation:
              there are two operation types:

              - topup: Increments the card balance.
              - withdrawal: Reduces the card balance.

          description: String field

          entity_id: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/cards/{card_id}/prepaid/operations",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "operation": operation,
                    "description": description,
                    "entity_id": entity_id,
                },
                operation_create_params.OperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        performed_at: operation_retrieve_params.PerformedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationRetrieveResponse:
        """
        Gets card balance operations

        Args:
          card_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          performed_at: Filters the operations by performed date and time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/v1/cards/{card_id}/prepaid/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "performed_at": performed_at,
                    },
                    operation_retrieve_params.OperationRetrieveParams,
                ),
            ),
            cast_to=OperationRetrieveResponse,
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_raw_response_wrapper(
            operations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            operations.retrieve,
        )


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_raw_response_wrapper(
            operations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            operations.retrieve,
        )


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_streamed_response_wrapper(
            operations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            operations.retrieve,
        )


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_streamed_response_wrapper(
            operations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            operations.retrieve,
        )
