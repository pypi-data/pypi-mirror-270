# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    required_args,
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
from ...types.spending_controls import rule_update_params
from ...types.spending_controls.rule_update_response import RuleUpdateResponse

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.VelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.VelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        weekly: rule_update_params.VelocitySchemaWeekly | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          daily: Limit amount for daily spending

          monthly: Limit amount for monthly spending

          weekly: Limit amount for weekly spending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        spending_control_id: str,
        *,
        disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]],
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.WithdrawalVelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.WithdrawalVelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          daily: Limit amount for daily withdrawal spending

          monthly: Limit amount for monthly withdrawal spending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["disabled_card_usages", "type"], ["type"])
    def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.VelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.VelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        weekly: rule_update_params.VelocitySchemaWeekly | NotGiven = NOT_GIVEN,
        disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return self._put(
            f"/v1/spending_controls/{spending_control_id}/rules",
            body=maybe_transform(
                {
                    "type": type,
                    "daily": daily,
                    "monthly": monthly,
                    "weekly": weekly,
                    "disabled_card_usages": disabled_card_usages,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleUpdateResponse,
        )

    def delete(
        self,
        type: Literal["velocity", "card_usage", "withdrawal_velocity"],
        *,
        spending_control_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to delete a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/spending_controls/{spending_control_id}/rules/{type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.VelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.VelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        weekly: rule_update_params.VelocitySchemaWeekly | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          daily: Limit amount for daily spending

          monthly: Limit amount for monthly spending

          weekly: Limit amount for weekly spending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        spending_control_id: str,
        *,
        disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]],
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.WithdrawalVelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.WithdrawalVelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        You can use this endpoint to add or update a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          type: String field

          daily: Limit amount for daily withdrawal spending

          monthly: Limit amount for monthly withdrawal spending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["disabled_card_usages", "type"], ["type"])
    async def update(
        self,
        spending_control_id: str,
        *,
        type: str,
        daily: rule_update_params.VelocitySchemaDaily | NotGiven = NOT_GIVEN,
        monthly: rule_update_params.VelocitySchemaMonthly | NotGiven = NOT_GIVEN,
        weekly: rule_update_params.VelocitySchemaWeekly | NotGiven = NOT_GIVEN,
        disabled_card_usages: List[Literal["online_purchase", "physical_purchase", "atm_withdrawal"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        return await self._put(
            f"/v1/spending_controls/{spending_control_id}/rules",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "daily": daily,
                    "monthly": monthly,
                    "weekly": weekly,
                    "disabled_card_usages": disabled_card_usages,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleUpdateResponse,
        )

    async def delete(
        self,
        type: Literal["velocity", "card_usage", "withdrawal_velocity"],
        *,
        spending_control_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to delete a rule to a spending control

        Args:
          spending_control_id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spending_control_id:
            raise ValueError(
                f"Expected a non-empty value for `spending_control_id` but received {spending_control_id!r}"
            )
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/spending_controls/{spending_control_id}/rules/{type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
