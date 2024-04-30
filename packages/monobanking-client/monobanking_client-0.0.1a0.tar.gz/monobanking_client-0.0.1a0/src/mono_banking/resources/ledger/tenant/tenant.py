# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TenantResource", "AsyncTenantResource"]


class TenantResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantResourceWithRawResponse:
        return TenantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantResourceWithStreamingResponse:
        return TenantResourceWithStreamingResponse(self)


class AsyncTenantResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantResourceWithRawResponse:
        return AsyncTenantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantResourceWithStreamingResponse:
        return AsyncTenantResourceWithStreamingResponse(self)


class TenantResourceWithRawResponse:
    def __init__(self, tenant: TenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._tenant.config)


class AsyncTenantResourceWithRawResponse:
    def __init__(self, tenant: AsyncTenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._tenant.config)


class TenantResourceWithStreamingResponse:
    def __init__(self, tenant: TenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._tenant.config)


class AsyncTenantResourceWithStreamingResponse:
    def __init__(self, tenant: AsyncTenantResource) -> None:
        self._tenant = tenant

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._tenant.config)
