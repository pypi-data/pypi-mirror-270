# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.cards.prepaid.balance_retrieve_response import BalanceRetrieveResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Gets card balance information

        Args:
          card_id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/v1/cards/{card_id}/prepaid/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceRetrieveResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Gets card balance information

        Args:
          card_id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/v1/cards/{card_id}/prepaid/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceRetrieveResponse,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve = to_raw_response_wrapper(
            balance.retrieve,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve = async_to_raw_response_wrapper(
            balance.retrieve,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve = to_streamed_response_wrapper(
            balance.retrieve,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve = async_to_streamed_response_wrapper(
            balance.retrieve,
        )
