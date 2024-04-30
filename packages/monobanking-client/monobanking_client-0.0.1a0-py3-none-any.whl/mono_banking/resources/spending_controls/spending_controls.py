# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ...types import (
    spending_control_list_params,
    spending_control_create_params,
    spending_control_update_params,
)
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
from .add_targets import (
    AddTargetsResource,
    AsyncAddTargetsResource,
    AddTargetsResourceWithRawResponse,
    AsyncAddTargetsResourceWithRawResponse,
    AddTargetsResourceWithStreamingResponse,
    AsyncAddTargetsResourceWithStreamingResponse,
)
from .list_targets import (
    ListTargetsResource,
    AsyncListTargetsResource,
    ListTargetsResourceWithRawResponse,
    AsyncListTargetsResourceWithRawResponse,
    ListTargetsResourceWithStreamingResponse,
    AsyncListTargetsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from .remove_targets import (
    RemoveTargetsResource,
    AsyncRemoveTargetsResource,
    RemoveTargetsResourceWithRawResponse,
    AsyncRemoveTargetsResourceWithRawResponse,
    RemoveTargetsResourceWithStreamingResponse,
    AsyncRemoveTargetsResourceWithStreamingResponse,
)
from ...types.spending_control_list_response import SpendingControlListResponse
from ...types.spending_control_create_response import SpendingControlCreateResponse
from ...types.spending_control_update_response import SpendingControlUpdateResponse

__all__ = ["SpendingControlsResource", "AsyncSpendingControlsResource"]


class SpendingControlsResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def list_targets(self) -> ListTargetsResource:
        return ListTargetsResource(self._client)

    @cached_property
    def add_targets(self) -> AddTargetsResource:
        return AddTargetsResource(self._client)

    @cached_property
    def remove_targets(self) -> RemoveTargetsResource:
        return RemoveTargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpendingControlsResourceWithRawResponse:
        return SpendingControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendingControlsResourceWithStreamingResponse:
        return SpendingControlsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency_code: Literal["COP", "USD", "MXN"],
        rules: spending_control_create_params.Rules,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        target: Literal["card"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlCreateResponse:
        """
        You can use this endpoint to create spending controls

        Args:
          currency_code: Spending control currency code

          rules: Configured spending control rules

          nickname: Spending control nickname

          target: Spending control target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/spending_controls",
            body=maybe_transform(
                {
                    "currency_code": currency_code,
                    "rules": rules,
                    "nickname": nickname,
                    "target": target,
                },
                spending_control_create_params.SpendingControlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlCreateResponse,
        )

    def update(
        self,
        spending_control_id: str,
        *,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlUpdateResponse:
        """
        You can use this endpoint to update a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          nickname: Spending control nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return self._patch(
            f"/v1/spending_controls/{spending_control_id}",
            body=maybe_transform({"nickname": nickname}, spending_control_update_params.SpendingControlUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        target: Literal["card"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlListResponse:
        """
        Gets all the Card spending controls

        Args:
          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          target: Target of the spending control

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/spending_controls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "target": target,
                    },
                    spending_control_list_params.SpendingControlListParams,
                ),
            ),
            cast_to=SpendingControlListResponse,
        )


class AsyncSpendingControlsResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def list_targets(self) -> AsyncListTargetsResource:
        return AsyncListTargetsResource(self._client)

    @cached_property
    def add_targets(self) -> AsyncAddTargetsResource:
        return AsyncAddTargetsResource(self._client)

    @cached_property
    def remove_targets(self) -> AsyncRemoveTargetsResource:
        return AsyncRemoveTargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpendingControlsResourceWithRawResponse:
        return AsyncSpendingControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendingControlsResourceWithStreamingResponse:
        return AsyncSpendingControlsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency_code: Literal["COP", "USD", "MXN"],
        rules: spending_control_create_params.Rules,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        target: Literal["card"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlCreateResponse:
        """
        You can use this endpoint to create spending controls

        Args:
          currency_code: Spending control currency code

          rules: Configured spending control rules

          nickname: Spending control nickname

          target: Spending control target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/spending_controls",
            body=await async_maybe_transform(
                {
                    "currency_code": currency_code,
                    "rules": rules,
                    "nickname": nickname,
                    "target": target,
                },
                spending_control_create_params.SpendingControlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlCreateResponse,
        )

    async def update(
        self,
        spending_control_id: str,
        *,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlUpdateResponse:
        """
        You can use this endpoint to update a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          nickname: Spending control nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return await self._patch(
            f"/v1/spending_controls/{spending_control_id}",
            body=await async_maybe_transform(
                {"nickname": nickname}, spending_control_update_params.SpendingControlUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendingControlUpdateResponse,
        )

    async def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        target: Literal["card"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpendingControlListResponse:
        """
        Gets all the Card spending controls

        Args:
          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          target: Target of the spending control

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/spending_controls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "target": target,
                    },
                    spending_control_list_params.SpendingControlListParams,
                ),
            ),
            cast_to=SpendingControlListResponse,
        )


class SpendingControlsResourceWithRawResponse:
    def __init__(self, spending_controls: SpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.create = to_raw_response_wrapper(
            spending_controls.create,
        )
        self.update = to_raw_response_wrapper(
            spending_controls.update,
        )
        self.list = to_raw_response_wrapper(
            spending_controls.list,
        )

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._spending_controls.rules)

    @cached_property
    def list_targets(self) -> ListTargetsResourceWithRawResponse:
        return ListTargetsResourceWithRawResponse(self._spending_controls.list_targets)

    @cached_property
    def add_targets(self) -> AddTargetsResourceWithRawResponse:
        return AddTargetsResourceWithRawResponse(self._spending_controls.add_targets)

    @cached_property
    def remove_targets(self) -> RemoveTargetsResourceWithRawResponse:
        return RemoveTargetsResourceWithRawResponse(self._spending_controls.remove_targets)


class AsyncSpendingControlsResourceWithRawResponse:
    def __init__(self, spending_controls: AsyncSpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.create = async_to_raw_response_wrapper(
            spending_controls.create,
        )
        self.update = async_to_raw_response_wrapper(
            spending_controls.update,
        )
        self.list = async_to_raw_response_wrapper(
            spending_controls.list,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._spending_controls.rules)

    @cached_property
    def list_targets(self) -> AsyncListTargetsResourceWithRawResponse:
        return AsyncListTargetsResourceWithRawResponse(self._spending_controls.list_targets)

    @cached_property
    def add_targets(self) -> AsyncAddTargetsResourceWithRawResponse:
        return AsyncAddTargetsResourceWithRawResponse(self._spending_controls.add_targets)

    @cached_property
    def remove_targets(self) -> AsyncRemoveTargetsResourceWithRawResponse:
        return AsyncRemoveTargetsResourceWithRawResponse(self._spending_controls.remove_targets)


class SpendingControlsResourceWithStreamingResponse:
    def __init__(self, spending_controls: SpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.create = to_streamed_response_wrapper(
            spending_controls.create,
        )
        self.update = to_streamed_response_wrapper(
            spending_controls.update,
        )
        self.list = to_streamed_response_wrapper(
            spending_controls.list,
        )

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._spending_controls.rules)

    @cached_property
    def list_targets(self) -> ListTargetsResourceWithStreamingResponse:
        return ListTargetsResourceWithStreamingResponse(self._spending_controls.list_targets)

    @cached_property
    def add_targets(self) -> AddTargetsResourceWithStreamingResponse:
        return AddTargetsResourceWithStreamingResponse(self._spending_controls.add_targets)

    @cached_property
    def remove_targets(self) -> RemoveTargetsResourceWithStreamingResponse:
        return RemoveTargetsResourceWithStreamingResponse(self._spending_controls.remove_targets)


class AsyncSpendingControlsResourceWithStreamingResponse:
    def __init__(self, spending_controls: AsyncSpendingControlsResource) -> None:
        self._spending_controls = spending_controls

        self.create = async_to_streamed_response_wrapper(
            spending_controls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            spending_controls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            spending_controls.list,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._spending_controls.rules)

    @cached_property
    def list_targets(self) -> AsyncListTargetsResourceWithStreamingResponse:
        return AsyncListTargetsResourceWithStreamingResponse(self._spending_controls.list_targets)

    @cached_property
    def add_targets(self) -> AsyncAddTargetsResourceWithStreamingResponse:
        return AsyncAddTargetsResourceWithStreamingResponse(self._spending_controls.add_targets)

    @cached_property
    def remove_targets(self) -> AsyncRemoveTargetsResourceWithStreamingResponse:
        return AsyncRemoveTargetsResourceWithStreamingResponse(self._spending_controls.remove_targets)
