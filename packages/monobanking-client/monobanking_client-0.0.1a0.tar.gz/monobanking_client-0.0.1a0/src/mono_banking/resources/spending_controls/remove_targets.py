# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.spending_controls import remove_target_delete_params

__all__ = ["RemoveTargetsResource", "AsyncRemoveTargetsResource"]


class RemoveTargetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RemoveTargetsResourceWithRawResponse:
        return RemoveTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemoveTargetsResourceWithStreamingResponse:
        return RemoveTargetsResourceWithStreamingResponse(self)

    def delete(
        self,
        spending_control_id: str,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to remove targets to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          ids: It contains a collection of target ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/spending_controls/{spending_control_id}/remove_targets",
            body=maybe_transform({"ids": ids}, remove_target_delete_params.RemoveTargetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRemoveTargetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRemoveTargetsResourceWithRawResponse:
        return AsyncRemoveTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemoveTargetsResourceWithStreamingResponse:
        return AsyncRemoveTargetsResourceWithStreamingResponse(self)

    async def delete(
        self,
        spending_control_id: str,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to remove targets to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          ids: It contains a collection of target ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/spending_controls/{spending_control_id}/remove_targets",
            body=await async_maybe_transform({"ids": ids}, remove_target_delete_params.RemoveTargetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RemoveTargetsResourceWithRawResponse:
    def __init__(self, remove_targets: RemoveTargetsResource) -> None:
        self._remove_targets = remove_targets

        self.delete = to_raw_response_wrapper(
            remove_targets.delete,
        )


class AsyncRemoveTargetsResourceWithRawResponse:
    def __init__(self, remove_targets: AsyncRemoveTargetsResource) -> None:
        self._remove_targets = remove_targets

        self.delete = async_to_raw_response_wrapper(
            remove_targets.delete,
        )


class RemoveTargetsResourceWithStreamingResponse:
    def __init__(self, remove_targets: RemoveTargetsResource) -> None:
        self._remove_targets = remove_targets

        self.delete = to_streamed_response_wrapper(
            remove_targets.delete,
        )


class AsyncRemoveTargetsResourceWithStreamingResponse:
    def __init__(self, remove_targets: AsyncRemoveTargetsResource) -> None:
        self._remove_targets = remove_targets

        self.delete = async_to_streamed_response_wrapper(
            remove_targets.delete,
        )
