# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ..._base_client import (
    make_request_options,
)
from ...types.transfers import prepare_create_params
from ...types.transfers.prepare_create_response import PrepareCreateResponse

__all__ = ["PrepareResource", "AsyncPrepareResource"]


class PrepareResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrepareResourceWithRawResponse:
        return PrepareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrepareResourceWithStreamingResponse:
        return PrepareResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        transfers: Iterable[prepare_create_params.Transfer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrepareCreateResponse:
        """
        Creates and leaves a batch of transfers pending for approval, these bank
        transfers can be between accounts of the same or different banks, which allows
        multiple transfers to be processed together in a single request. This endpoint
        is designed to allow transfers to be reviewed and approved by an administrator
        user from the Mono app before being sent to the banks.

        When the server receives the request, it will process the batch of transfers and
        create transfer records in our database for each of them, the transfers will not
        be executed immediately, instead, the batch will be queued for review and
        approval by an administrator user from Mono app.

        Considerations:

        1. API key roles allowed to consume this endpoint are "Administrator" and
           "Preparer".
        2. The minimum number of transfers allowed per batch is 1.
        3. The maximum number of transfers allowed per batch are 1.000.

        Args:
          account_id: Represents the account of the client to which a debit entry will be made as a
              result of the transaction.

          transfers: It contains a list with transfers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/transfers/prepare",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "transfers": transfers,
                },
                prepare_create_params.PrepareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrepareCreateResponse,
        )


class AsyncPrepareResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrepareResourceWithRawResponse:
        return AsyncPrepareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrepareResourceWithStreamingResponse:
        return AsyncPrepareResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        transfers: Iterable[prepare_create_params.Transfer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrepareCreateResponse:
        """
        Creates and leaves a batch of transfers pending for approval, these bank
        transfers can be between accounts of the same or different banks, which allows
        multiple transfers to be processed together in a single request. This endpoint
        is designed to allow transfers to be reviewed and approved by an administrator
        user from the Mono app before being sent to the banks.

        When the server receives the request, it will process the batch of transfers and
        create transfer records in our database for each of them, the transfers will not
        be executed immediately, instead, the batch will be queued for review and
        approval by an administrator user from Mono app.

        Considerations:

        1. API key roles allowed to consume this endpoint are "Administrator" and
           "Preparer".
        2. The minimum number of transfers allowed per batch is 1.
        3. The maximum number of transfers allowed per batch are 1.000.

        Args:
          account_id: Represents the account of the client to which a debit entry will be made as a
              result of the transaction.

          transfers: It contains a list with transfers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/transfers/prepare",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "transfers": transfers,
                },
                prepare_create_params.PrepareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrepareCreateResponse,
        )


class PrepareResourceWithRawResponse:
    def __init__(self, prepare: PrepareResource) -> None:
        self._prepare = prepare

        self.create = to_raw_response_wrapper(
            prepare.create,
        )


class AsyncPrepareResourceWithRawResponse:
    def __init__(self, prepare: AsyncPrepareResource) -> None:
        self._prepare = prepare

        self.create = async_to_raw_response_wrapper(
            prepare.create,
        )


class PrepareResourceWithStreamingResponse:
    def __init__(self, prepare: PrepareResource) -> None:
        self._prepare = prepare

        self.create = to_streamed_response_wrapper(
            prepare.create,
        )


class AsyncPrepareResourceWithStreamingResponse:
    def __init__(self, prepare: AsyncPrepareResource) -> None:
        self._prepare = prepare

        self.create = async_to_streamed_response_wrapper(
            prepare.create,
        )
