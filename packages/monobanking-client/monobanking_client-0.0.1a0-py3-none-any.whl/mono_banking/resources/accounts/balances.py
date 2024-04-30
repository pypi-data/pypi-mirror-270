# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.accounts import balance_retrieve_params
from ...types.accounts.balance_retrieve_response import BalanceRetrieveResponse

__all__ = ["BalancesResource", "AsyncBalancesResource"]


class BalancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesResourceWithRawResponse:
        return BalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesResourceWithStreamingResponse:
        return BalancesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        live: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Get account balance

        Args:
          account_id: Indicates the format for resource's ID

          live: if true this will go to the bank and return the `real time` balance otherwise it
              will return the cached balance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/v1/accounts/{account_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"live": live}, balance_retrieve_params.BalanceRetrieveParams),
            ),
            cast_to=BalanceRetrieveResponse,
        )


class AsyncBalancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesResourceWithRawResponse:
        return AsyncBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesResourceWithStreamingResponse:
        return AsyncBalancesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        live: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Get account balance

        Args:
          account_id: Indicates the format for resource's ID

          live: if true this will go to the bank and return the `real time` balance otherwise it
              will return the cached balance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/v1/accounts/{account_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"live": live}, balance_retrieve_params.BalanceRetrieveParams),
            ),
            cast_to=BalanceRetrieveResponse,
        )


class BalancesResourceWithRawResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.retrieve = to_raw_response_wrapper(
            balances.retrieve,
        )


class AsyncBalancesResourceWithRawResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.retrieve = async_to_raw_response_wrapper(
            balances.retrieve,
        )


class BalancesResourceWithStreamingResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.retrieve = to_streamed_response_wrapper(
            balances.retrieve,
        )


class AsyncBalancesResourceWithStreamingResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.retrieve = async_to_streamed_response_wrapper(
            balances.retrieve,
        )
