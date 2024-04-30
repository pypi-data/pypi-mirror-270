# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tenant import (
    TenantResource,
    AsyncTenantResource,
    TenantResourceWithRawResponse,
    AsyncTenantResourceWithRawResponse,
    TenantResourceWithStreamingResponse,
    AsyncTenantResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .tenant.tenant import TenantResource, AsyncTenantResource
from .account_holders import (
    AccountHoldersResource,
    AsyncAccountHoldersResource,
    AccountHoldersResourceWithRawResponse,
    AsyncAccountHoldersResourceWithRawResponse,
    AccountHoldersResourceWithStreamingResponse,
    AsyncAccountHoldersResourceWithStreamingResponse,
)
from .accounts.accounts import AccountsResource, AsyncAccountsResource

__all__ = ["LedgerResource", "AsyncLedgerResource"]


class LedgerResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def account_holders(self) -> AccountHoldersResource:
        return AccountHoldersResource(self._client)

    @cached_property
    def tenant(self) -> TenantResource:
        return TenantResource(self._client)

    @cached_property
    def with_raw_response(self) -> LedgerResourceWithRawResponse:
        return LedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerResourceWithStreamingResponse:
        return LedgerResourceWithStreamingResponse(self)


class AsyncLedgerResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def account_holders(self) -> AsyncAccountHoldersResource:
        return AsyncAccountHoldersResource(self._client)

    @cached_property
    def tenant(self) -> AsyncTenantResource:
        return AsyncTenantResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLedgerResourceWithRawResponse:
        return AsyncLedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerResourceWithStreamingResponse:
        return AsyncLedgerResourceWithStreamingResponse(self)


class LedgerResourceWithRawResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._ledger.accounts)

    @cached_property
    def account_holders(self) -> AccountHoldersResourceWithRawResponse:
        return AccountHoldersResourceWithRawResponse(self._ledger.account_holders)

    @cached_property
    def tenant(self) -> TenantResourceWithRawResponse:
        return TenantResourceWithRawResponse(self._ledger.tenant)


class AsyncLedgerResourceWithRawResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._ledger.accounts)

    @cached_property
    def account_holders(self) -> AsyncAccountHoldersResourceWithRawResponse:
        return AsyncAccountHoldersResourceWithRawResponse(self._ledger.account_holders)

    @cached_property
    def tenant(self) -> AsyncTenantResourceWithRawResponse:
        return AsyncTenantResourceWithRawResponse(self._ledger.tenant)


class LedgerResourceWithStreamingResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._ledger.accounts)

    @cached_property
    def account_holders(self) -> AccountHoldersResourceWithStreamingResponse:
        return AccountHoldersResourceWithStreamingResponse(self._ledger.account_holders)

    @cached_property
    def tenant(self) -> TenantResourceWithStreamingResponse:
        return TenantResourceWithStreamingResponse(self._ledger.tenant)


class AsyncLedgerResourceWithStreamingResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._ledger.accounts)

    @cached_property
    def account_holders(self) -> AsyncAccountHoldersResourceWithStreamingResponse:
        return AsyncAccountHoldersResourceWithStreamingResponse(self._ledger.account_holders)

    @cached_property
    def tenant(self) -> AsyncTenantResourceWithStreamingResponse:
        return AsyncTenantResourceWithStreamingResponse(self._ledger.tenant)
