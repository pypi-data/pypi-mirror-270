# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ....types.ledger.accounts import balance_topup_or_withdraw_params
from ....types.ledger.accounts.balance_topup_or_withdraw_response import BalanceTopupOrWithdrawResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self)

    def topup_or_withdraw(
        self,
        account_id: str,
        *,
        amount: balance_topup_or_withdraw_params.Amount,
        external_id: str,
        operation: Literal["topup", "withdrawal"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceTopupOrWithdrawResponse:
        """Topup or withdraw a ledger account balance.

        Considerations:

        1.

        This endpoint could be only used for accounts with type `subaccount`.
        2. The accounts should be `active`.
        3. The associated account holder should also be `active`.
        4. You can only make operations if the currency code of the amount is the same
           as the currency code of the account.

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          external_id: Unique identifier of the update balance operation

          operation: Operation type to perform an update balance, it can be one of the following
              options:

              - `topup`: Increment the account balance.
              - `withdrawal`: Decrease the account balance.

          description: String field

          reference: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/v1/ledger/accounts/{account_id}/balance",
            body=maybe_transform(
                {
                    "amount": amount,
                    "external_id": external_id,
                    "operation": operation,
                    "description": description,
                    "reference": reference,
                },
                balance_topup_or_withdraw_params.BalanceTopupOrWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceTopupOrWithdrawResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def topup_or_withdraw(
        self,
        account_id: str,
        *,
        amount: balance_topup_or_withdraw_params.Amount,
        external_id: str,
        operation: Literal["topup", "withdrawal"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceTopupOrWithdrawResponse:
        """Topup or withdraw a ledger account balance.

        Considerations:

        1.

        This endpoint could be only used for accounts with type `subaccount`.
        2. The accounts should be `active`.
        3. The associated account holder should also be `active`.
        4. You can only make operations if the currency code of the amount is the same
           as the currency code of the account.

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          external_id: Unique identifier of the update balance operation

          operation: Operation type to perform an update balance, it can be one of the following
              options:

              - `topup`: Increment the account balance.
              - `withdrawal`: Decrease the account balance.

          description: String field

          reference: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/v1/ledger/accounts/{account_id}/balance",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "external_id": external_id,
                    "operation": operation,
                    "description": description,
                    "reference": reference,
                },
                balance_topup_or_withdraw_params.BalanceTopupOrWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceTopupOrWithdrawResponse,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.topup_or_withdraw = to_raw_response_wrapper(
            balance.topup_or_withdraw,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.topup_or_withdraw = async_to_raw_response_wrapper(
            balance.topup_or_withdraw,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.topup_or_withdraw = to_streamed_response_wrapper(
            balance.topup_or_withdraw,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.topup_or_withdraw = async_to_streamed_response_wrapper(
            balance.topup_or_withdraw,
        )
