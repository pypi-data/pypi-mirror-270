# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, cast
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
from ....types.ledger.accounts import transaction_list_params
from ....types.ledger.accounts.transaction_list_response import TransactionListResponse
from ....types.ledger.accounts.transaction_retrieve_response import TransactionRetrieveResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Gets an account transaction detail

        Args:
          account_id: Indicates the format for resource's ID

          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            TransactionRetrieveResponse,
            self._get(
                f"/v1/ledger/accounts/{account_id}/transactions/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TransactionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        account_id: str,
        *,
        operation_type: Union[
            List[Literal["debit", "credit", "hold", "release"]], Literal["debit", "credit", "hold", "release"]
        ]
        | NotGiven = NOT_GIVEN,
        origin: Union[List[str], str] | NotGiven = NOT_GIVEN,
        origin_transaction_at: transaction_list_params.OriginTransactionAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort: transaction_list_params.Sort | NotGiven = NOT_GIVEN,
        transaction_at: transaction_list_params.TransactionAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionListResponse:
        """
        Gets account transactions

        Args:
          account_id: Indicates the format for resource's ID

          operation_type: Filters by the four operations available (credit, debit, hold and release)

          origin: Filters by the origins like `card_transaction`, `card_authorization`, etc.

          origin_transaction_at: Filters the transactions by date time ranges when the transaction was created

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          sort: Sorts the ledger account transactions

          transaction_at: Filters the transactions by date time ranges when the transaction was actually
              performed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/v1/ledger/accounts/{account_id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "operation_type": operation_type,
                        "origin": origin,
                        "origin_transaction_at": origin_transaction_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
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

    async def retrieve(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Gets an account transaction detail

        Args:
          account_id: Indicates the format for resource's ID

          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            TransactionRetrieveResponse,
            await self._get(
                f"/v1/ledger/accounts/{account_id}/transactions/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, TransactionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        account_id: str,
        *,
        operation_type: Union[
            List[Literal["debit", "credit", "hold", "release"]], Literal["debit", "credit", "hold", "release"]
        ]
        | NotGiven = NOT_GIVEN,
        origin: Union[List[str], str] | NotGiven = NOT_GIVEN,
        origin_transaction_at: transaction_list_params.OriginTransactionAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort: transaction_list_params.Sort | NotGiven = NOT_GIVEN,
        transaction_at: transaction_list_params.TransactionAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionListResponse:
        """
        Gets account transactions

        Args:
          account_id: Indicates the format for resource's ID

          operation_type: Filters by the four operations available (credit, debit, hold and release)

          origin: Filters by the origins like `card_transaction`, `card_authorization`, etc.

          origin_transaction_at: Filters the transactions by date time ranges when the transaction was created

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          sort: Sorts the ledger account transactions

          transaction_at: Filters the transactions by date time ranges when the transaction was actually
              performed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/v1/ledger/accounts/{account_id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "operation_type": operation_type,
                        "origin": origin,
                        "origin_transaction_at": origin_transaction_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
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

        self.retrieve = to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
