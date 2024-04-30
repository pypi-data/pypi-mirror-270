# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.v1.spending_control_retrieve_response import SpendingControlRetrieveResponse

__all__ = ["SpendingControlsResource", "AsyncSpendingControlsResource"]


class SpendingControlsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpendingControlsResourceWithRawResponse:
        return SpendingControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendingControlsResourceWithStreamingResponse:
        return SpendingControlsResourceWithStreamingResponse(self)

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
    ) -> SpendingControlRetrieveResponse:
        """
        You can use this endpoint to get a spending control

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
            f"/v1/spending_controls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlRetrieveResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to delete a spending control

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/spending_controls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSpendingControlsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpendingControlsResourceWithRawResponse:
        return AsyncSpendingControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendingControlsResourceWithStreamingResponse:
        return AsyncSpendingControlsResourceWithStreamingResponse(self)

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
    ) -> SpendingControlRetrieveResponse:
        """
        You can use this endpoint to get a spending control

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
            f"/v1/spending_controls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlRetrieveResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to delete a spending control

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/spending_controls/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SpendingControlsResourceWithRawResponse:
    def __init__(self, spending_controls: SpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.retrieve = to_raw_response_wrapper(
            spending_controls.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            spending_controls.delete,
        )


class AsyncSpendingControlsResourceWithRawResponse:
    def __init__(self, spending_controls: AsyncSpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.retrieve = async_to_raw_response_wrapper(
            spending_controls.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            spending_controls.delete,
        )


class SpendingControlsResourceWithStreamingResponse:
    def __init__(self, spending_controls: SpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.retrieve = to_streamed_response_wrapper(
            spending_controls.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            spending_controls.delete,
        )


class AsyncSpendingControlsResourceWithStreamingResponse:
    def __init__(self, spending_controls: AsyncSpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.retrieve = async_to_streamed_response_wrapper(
            spending_controls.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            spending_controls.delete,
        )
