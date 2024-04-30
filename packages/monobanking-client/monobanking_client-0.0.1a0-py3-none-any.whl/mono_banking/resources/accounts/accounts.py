# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .balances import (
    BalancesResource,
    AsyncBalancesResource,
    BalancesResourceWithRawResponse,
    AsyncBalancesResourceWithRawResponse,
    BalancesResourceWithStreamingResponse,
    AsyncBalancesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def balances(self) -> BalancesResource:
        return BalancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def balances(self) -> AsyncBalancesResource:
        return AsyncBalancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def balances(self) -> BalancesResourceWithRawResponse:
        return BalancesResourceWithRawResponse(self._accounts.balances)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithRawResponse:
        return AsyncBalancesResourceWithRawResponse(self._accounts.balances)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def balances(self) -> BalancesResourceWithStreamingResponse:
        return BalancesResourceWithStreamingResponse(self._accounts.balances)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithStreamingResponse:
        return AsyncBalancesResourceWithStreamingResponse(self._accounts.balances)
