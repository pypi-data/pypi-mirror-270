# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.v1.ledger import account_update_params
from ....types.v1.ledger.account_update_response import AccountUpdateResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        state: Literal["active", "blocked"],
        detail: str | NotGiven = NOT_GIVEN,
        reason: Literal["temporary", "user_request", "unused", "fraud", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Updates state of a subaccount type ledger account.

        Considerations:

        1.

        You couldn't modify state of the canceled ledger accounts.
        2. You couldn't modify accounts where the type is different of a `subaccount`

        Args:
          id: Indicates the format for resource's ID

          state:
              State to update the account, it can be one of the following values:

              - active: it's enabled to perform operations with the account balance.
              - blocked: it's disabled by a tenant and couldn't perform any operation with the
                account balance.

          detail: It provides a textual reason why the account is blocked in case of the
              state_reason value is `other`.

          reason: It provides the reason why the account could be blocked. It is required when the
              account is transitioned to being blocked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/ledger/accounts/{id}",
            body=maybe_transform(
                {
                    "state": state,
                    "detail": detail,
                    "reason": reason,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        state: Literal["active", "blocked"],
        detail: str | NotGiven = NOT_GIVEN,
        reason: Literal["temporary", "user_request", "unused", "fraud", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Updates state of a subaccount type ledger account.

        Considerations:

        1.

        You couldn't modify state of the canceled ledger accounts.
        2. You couldn't modify accounts where the type is different of a `subaccount`

        Args:
          id: Indicates the format for resource's ID

          state:
              State to update the account, it can be one of the following values:

              - active: it's enabled to perform operations with the account balance.
              - blocked: it's disabled by a tenant and couldn't perform any operation with the
                account balance.

          detail: It provides a textual reason why the account is blocked in case of the
              state_reason value is `other`.

          reason: It provides the reason why the account could be blocked. It is required when the
              account is transitioned to being blocked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/ledger/accounts/{id}",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "detail": detail,
                    "reason": reason,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_raw_response_wrapper(
            accounts.update,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_streamed_response_wrapper(
            accounts.update,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
