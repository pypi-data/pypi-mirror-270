# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from .balances import (
    BalancesResource,
    AsyncBalancesResource,
    BalancesResourceWithRawResponse,
    AsyncBalancesResourceWithRawResponse,
    BalancesResourceWithStreamingResponse,
    AsyncBalancesResourceWithStreamingResponse,
)
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
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.ledger import account_list_params, account_create_params
from ....types.ledger.account_list_response import AccountListResponse
from ....types.ledger.account_create_response import AccountCreateResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def balances(self) -> BalancesResource:
        return BalancesResource(self._client)

    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency_code: Literal["COP", "USD", "MXN"],
        holder_id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Creates a ledger account associated to a third-party account holder.

        Considerations:

        1. You could previusly check the accepted currency codes in the endpoint
           `/v1/ledger/tenant/config`.
        2. The third-party account holder must be `active`.

        Args:
          currency_code: The currency associated with the account balance.

          holder_id: Identifier of the third-party account holder.

          name: Name of the account, which is used to describe the account's purpose better.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ledger/accounts",
            body=maybe_transform(
                {
                    "currency_code": currency_code,
                    "holder_id": holder_id,
                    "name": name,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    def list(
        self,
        *,
        currency_code: List[Literal["COP", "USD", "MXN"]] | NotGiven = NOT_GIVEN,
        holder: List[str] | NotGiven = NOT_GIVEN,
        inserted_at: account_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        nickname: account_list_params.Nickname | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: List[Literal["active", "blocked", "canceled"]] | NotGiven = NOT_GIVEN,
        type: List[Literal["subaccount", "current", "bank_settlement", "trade_account", "virtual_settlement"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Lists all the ledger accounts related to the tenant

        Considerations:

        1.

        This endpoint doesn't return the account balance for every account, so you
           can use the endpoint to get the balance for a specific account
           `/v1/ledger/account/:id/balances`
        2. You couldn't retrieve more than 500 registers in a single request.

        Args:
          currency_code: Filter by the account's currency code

          holder: Filter by account holder ID

          inserted_at: Filter accounts based on the range of insertion date and time.

          nickname: Filter by account's name

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filter by the account's state

          type: Filter by account's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ledger/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_code": currency_code,
                        "holder": holder,
                        "inserted_at": inserted_at,
                        "nickname": nickname,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                        "type": type,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def balances(self) -> AsyncBalancesResource:
        return AsyncBalancesResource(self._client)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency_code: Literal["COP", "USD", "MXN"],
        holder_id: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Creates a ledger account associated to a third-party account holder.

        Considerations:

        1. You could previusly check the accepted currency codes in the endpoint
           `/v1/ledger/tenant/config`.
        2. The third-party account holder must be `active`.

        Args:
          currency_code: The currency associated with the account balance.

          holder_id: Identifier of the third-party account holder.

          name: Name of the account, which is used to describe the account's purpose better.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ledger/accounts",
            body=await async_maybe_transform(
                {
                    "currency_code": currency_code,
                    "holder_id": holder_id,
                    "name": name,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    async def list(
        self,
        *,
        currency_code: List[Literal["COP", "USD", "MXN"]] | NotGiven = NOT_GIVEN,
        holder: List[str] | NotGiven = NOT_GIVEN,
        inserted_at: account_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        nickname: account_list_params.Nickname | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: List[Literal["active", "blocked", "canceled"]] | NotGiven = NOT_GIVEN,
        type: List[Literal["subaccount", "current", "bank_settlement", "trade_account", "virtual_settlement"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Lists all the ledger accounts related to the tenant

        Considerations:

        1.

        This endpoint doesn't return the account balance for every account, so you
           can use the endpoint to get the balance for a specific account
           `/v1/ledger/account/:id/balances`
        2. You couldn't retrieve more than 500 registers in a single request.

        Args:
          currency_code: Filter by the account's currency code

          holder: Filter by account holder ID

          inserted_at: Filter accounts based on the range of insertion date and time.

          nickname: Filter by account's name

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filter by the account's state

          type: Filter by account's type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ledger/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency_code": currency_code,
                        "holder": holder,
                        "inserted_at": inserted_at,
                        "nickname": nickname,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                        "type": type,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithRawResponse:
        return BalancesResourceWithRawResponse(self._accounts.balances)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._accounts.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._accounts.balance)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithRawResponse:
        return AsyncBalancesResourceWithRawResponse(self._accounts.balances)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._accounts.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._accounts.balance)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithStreamingResponse:
        return BalancesResourceWithStreamingResponse(self._accounts.balances)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._accounts.transactions)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._accounts.balance)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithStreamingResponse:
        return AsyncBalancesResourceWithStreamingResponse(self._accounts.balances)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._accounts.transactions)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._accounts.balance)
