# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.v1.cards import transaction_list_params
from ....types.v1.cards.transaction_list_response import TransactionListResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self)

    def list(
        self,
        card_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Literal["approved", "reversed", "declined"] | NotGiven = NOT_GIVEN,
        transaction_at: transaction_list_params.TransactionAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionListResponse:
        """
        Gets card transactions

        Args:
          card_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filters the transactions by date and time when the transaction was made

          transaction_at: Filters the transactions by date and time when the transaction was made

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/v1/cards/{card_id}/transactions",
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
                        "transaction_at": transaction_at,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def list(
        self,
        card_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Literal["approved", "reversed", "declined"] | NotGiven = NOT_GIVEN,
        transaction_at: transaction_list_params.TransactionAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionListResponse:
        """
        Gets card transactions

        Args:
          card_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filters the transactions by date and time when the transaction was made

          transaction_at: Filters the transactions by date and time when the transaction was made

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/v1/cards/{card_id}/transactions",
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
                        "transaction_at": transaction_at,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.list = to_raw_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.list = to_streamed_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
