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
from ...types.spending_controls import list_target_retrieve_params
from ...types.spending_controls.list_target_retrieve_response import ListTargetRetrieveResponse

__all__ = ["ListTargetsResource", "AsyncListTargetsResource"]


class ListTargetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListTargetsResourceWithRawResponse:
        return ListTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListTargetsResourceWithStreamingResponse:
        return ListTargetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        spending_control_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListTargetRetrieveResponse:
        """
        You can use this endpoint to list spending control's targets

        Args:
          spending_control_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return self._get(
            f"/v1/spending_controls/{spending_control_id}/list_targets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    list_target_retrieve_params.ListTargetRetrieveParams,
                ),
            ),
            cast_to=ListTargetRetrieveResponse,
        )


class AsyncListTargetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListTargetsResourceWithRawResponse:
        return AsyncListTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListTargetsResourceWithStreamingResponse:
        return AsyncListTargetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        spending_control_id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListTargetRetrieveResponse:
        """
        You can use this endpoint to list spending control's targets

        Args:
          spending_control_id: Indicates the format for resource's ID

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return await self._get(
            f"/v1/spending_controls/{spending_control_id}/list_targets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    list_target_retrieve_params.ListTargetRetrieveParams,
                ),
            ),
            cast_to=ListTargetRetrieveResponse,
        )


class ListTargetsResourceWithRawResponse:
    def __init__(self, list_targets: ListTargetsResource) -> None:
        self._list_targets = list_targets

        self.retrieve = to_raw_response_wrapper(
            list_targets.retrieve,
        )


class AsyncListTargetsResourceWithRawResponse:
    def __init__(self, list_targets: AsyncListTargetsResource) -> None:
        self._list_targets = list_targets

        self.retrieve = async_to_raw_response_wrapper(
            list_targets.retrieve,
        )


class ListTargetsResourceWithStreamingResponse:
    def __init__(self, list_targets: ListTargetsResource) -> None:
        self._list_targets = list_targets

        self.retrieve = to_streamed_response_wrapper(
            list_targets.retrieve,
        )


class AsyncListTargetsResourceWithStreamingResponse:
    def __init__(self, list_targets: AsyncListTargetsResource) -> None:
        self._list_targets = list_targets

        self.retrieve = async_to_streamed_response_wrapper(
            list_targets.retrieve,
        )
