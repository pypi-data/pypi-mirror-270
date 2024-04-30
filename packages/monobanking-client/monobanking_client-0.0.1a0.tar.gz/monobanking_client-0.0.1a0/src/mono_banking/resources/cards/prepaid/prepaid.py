# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PrepaidResource", "AsyncPrepaidResource"]


class PrepaidResource(SyncAPIResource):
    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrepaidResourceWithRawResponse:
        return PrepaidResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrepaidResourceWithStreamingResponse:
        return PrepaidResourceWithStreamingResponse(self)


class AsyncPrepaidResource(AsyncAPIResource):
    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrepaidResourceWithRawResponse:
        return AsyncPrepaidResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrepaidResourceWithStreamingResponse:
        return AsyncPrepaidResourceWithStreamingResponse(self)


class PrepaidResourceWithRawResponse:
    def __init__(self, prepaid: PrepaidResource) -> None:
        self._prepaid = prepaid

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._prepaid.balance)

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._prepaid.operations)


class AsyncPrepaidResourceWithRawResponse:
    def __init__(self, prepaid: AsyncPrepaidResource) -> None:
        self._prepaid = prepaid

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._prepaid.balance)

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._prepaid.operations)


class PrepaidResourceWithStreamingResponse:
    def __init__(self, prepaid: PrepaidResource) -> None:
        self._prepaid = prepaid

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._prepaid.balance)

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._prepaid.operations)


class AsyncPrepaidResourceWithStreamingResponse:
    def __init__(self, prepaid: AsyncPrepaidResource) -> None:
        self._prepaid = prepaid

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._prepaid.balance)

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._prepaid.operations)
