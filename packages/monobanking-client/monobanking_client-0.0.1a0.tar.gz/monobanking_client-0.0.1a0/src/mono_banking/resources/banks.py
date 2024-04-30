# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import bank_list_params
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
from ..types.bank_list_response import BankListResponse

__all__ = ["BanksResource", "AsyncBanksResource"]


class BanksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BanksResourceWithRawResponse:
        return BanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BanksResourceWithStreamingResponse:
        return BanksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        kind: Literal["transfers", "pse"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BankListResponse:
        """
        Whenever you want to prepare or apply a transfer and make a collection, you need
        to specify the `code` of the bank to which you want to transfer money or make
        the collection. This endpoint retrieves all the target banks we support with the
        necessary `code` you need to provide for bank transfer or collection endpoints.

        This endpoint also retrieves the supported account type for each bank you can
        transfer to (only if the `kind` parameter is `transfers`).

        Args:
          kind: there are two types of responses (Polymorphism response) the first `transfers`
              are the banks used by the bank transfers and the `pse` are the banks from the
              pse provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            BankListResponse,
            self._get(
                "/v1/banks",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"kind": kind}, bank_list_params.BankListParams),
                ),
                cast_to=cast(Any, BankListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBanksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBanksResourceWithRawResponse:
        return AsyncBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBanksResourceWithStreamingResponse:
        return AsyncBanksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        kind: Literal["transfers", "pse"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BankListResponse:
        """
        Whenever you want to prepare or apply a transfer and make a collection, you need
        to specify the `code` of the bank to which you want to transfer money or make
        the collection. This endpoint retrieves all the target banks we support with the
        necessary `code` you need to provide for bank transfer or collection endpoints.

        This endpoint also retrieves the supported account type for each bank you can
        transfer to (only if the `kind` parameter is `transfers`).

        Args:
          kind: there are two types of responses (Polymorphism response) the first `transfers`
              are the banks used by the bank transfers and the `pse` are the banks from the
              pse provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            BankListResponse,
            await self._get(
                "/v1/banks",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"kind": kind}, bank_list_params.BankListParams),
                ),
                cast_to=cast(Any, BankListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BanksResourceWithRawResponse:
    def __init__(self, banks: BanksResource) -> None:
        self._banks = banks

        self.list = to_raw_response_wrapper(
            banks.list,
        )


class AsyncBanksResourceWithRawResponse:
    def __init__(self, banks: AsyncBanksResource) -> None:
        self._banks = banks

        self.list = async_to_raw_response_wrapper(
            banks.list,
        )


class BanksResourceWithStreamingResponse:
    def __init__(self, banks: BanksResource) -> None:
        self._banks = banks

        self.list = to_streamed_response_wrapper(
            banks.list,
        )


class AsyncBanksResourceWithStreamingResponse:
    def __init__(self, banks: AsyncBanksResource) -> None:
        self._banks = banks

        self.list = async_to_streamed_response_wrapper(
            banks.list,
        )
