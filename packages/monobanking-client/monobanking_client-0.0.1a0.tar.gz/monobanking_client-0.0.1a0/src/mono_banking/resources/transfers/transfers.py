# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import transfer_list_params, transfer_create_params
from .prepare import (
    PrepareResource,
    AsyncPrepareResource,
    PrepareResourceWithRawResponse,
    AsyncPrepareResourceWithRawResponse,
    PrepareResourceWithStreamingResponse,
    AsyncPrepareResourceWithStreamingResponse,
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
from ..._base_client import (
    make_request_options,
)
from ...types.transfer_list_response import TransferListResponse
from ...types.transfer_create_response import TransferCreateResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def prepare(self) -> PrepareResource:
        return PrepareResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        transfers: Iterable[transfer_create_params.Transfer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferCreateResponse:
        """
        Creates and sends a batch of bank transfers without the requiring of an
        additional authorization, this can be between accounts of the same or different
        banks, which allows multiple transfers to be processed together in a single
        request.

        When the server receives the request, it will process it and initiate the
        transfer of funds between the source and destination bank accounts. This
        involves debiting the appropriate amount from the source account, and crediting
        the destination account with the transferred funds.

        This endpoint is used in cases where the client wants to initiate bank transfers
        from their own system or application, without the need to log in to their bank's
        website or use a separate banking app. This can be useful for a variety of
        purposes, such as to automate financial operations, to streamline the payment
        process, or to provide a more convenient user experience.

        Considerations:

        1. API key role allowed to consume this endpoint is "Administrator".
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
            "/v1/transfers",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "transfers": transfers,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferCreateResponse,
        )

    def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        batch_id: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        inserted_at: transfer_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payee_account_number: str | NotGiven = NOT_GIVEN,
        payee_document: transfer_list_params.PayeeDocument | NotGiven = NOT_GIVEN,
        sort: transfer_list_params.Sort | NotGiven = NOT_GIVEN,
        state: Literal["created", "in_progress", "cancelled", "declined", "approved", "duplicated"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferListResponse:
        """List bank transfers of your organization.

        This endpoint allows to filters, sort,
        and control pagination of the transfers you want to fetch.

        Considerations:

        - API key roles allowed to consume this endpoint are "Administrator",
          "Preparer", and "Viewer".

        Args:
          id: Filters by the transfer ID

          account_id: Filters base on the bank account that money was moved from

          batch_id: Filters transfers by the specific batch were sent

          entity_id: Filters by entity ID

          inserted_at: Filters transfers base on creation datetime

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          payee_account_number: Filters the transfers by a specific payee's bank account

          payee_document: Filters the transfers by a specific payee's national document. Number and type
              must be provided at the same time.

          sort: Sorts transfers depending on the types and fields

          state: Filters the transfers by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/transfers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "account_id": account_id,
                        "batch_id": batch_id,
                        "entity_id": entity_id,
                        "inserted_at": inserted_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "payee_account_number": payee_account_number,
                        "payee_document": payee_document,
                        "sort": sort,
                        "state": state,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=TransferListResponse,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def prepare(self) -> AsyncPrepareResource:
        return AsyncPrepareResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        transfers: Iterable[transfer_create_params.Transfer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferCreateResponse:
        """
        Creates and sends a batch of bank transfers without the requiring of an
        additional authorization, this can be between accounts of the same or different
        banks, which allows multiple transfers to be processed together in a single
        request.

        When the server receives the request, it will process it and initiate the
        transfer of funds between the source and destination bank accounts. This
        involves debiting the appropriate amount from the source account, and crediting
        the destination account with the transferred funds.

        This endpoint is used in cases where the client wants to initiate bank transfers
        from their own system or application, without the need to log in to their bank's
        website or use a separate banking app. This can be useful for a variety of
        purposes, such as to automate financial operations, to streamline the payment
        process, or to provide a more convenient user experience.

        Considerations:

        1. API key role allowed to consume this endpoint is "Administrator".
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
            "/v1/transfers",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "transfers": transfers,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferCreateResponse,
        )

    async def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        batch_id: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        inserted_at: transfer_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payee_account_number: str | NotGiven = NOT_GIVEN,
        payee_document: transfer_list_params.PayeeDocument | NotGiven = NOT_GIVEN,
        sort: transfer_list_params.Sort | NotGiven = NOT_GIVEN,
        state: Literal["created", "in_progress", "cancelled", "declined", "approved", "duplicated"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferListResponse:
        """List bank transfers of your organization.

        This endpoint allows to filters, sort,
        and control pagination of the transfers you want to fetch.

        Considerations:

        - API key roles allowed to consume this endpoint are "Administrator",
          "Preparer", and "Viewer".

        Args:
          id: Filters by the transfer ID

          account_id: Filters base on the bank account that money was moved from

          batch_id: Filters transfers by the specific batch were sent

          entity_id: Filters by entity ID

          inserted_at: Filters transfers base on creation datetime

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          payee_account_number: Filters the transfers by a specific payee's bank account

          payee_document: Filters the transfers by a specific payee's national document. Number and type
              must be provided at the same time.

          sort: Sorts transfers depending on the types and fields

          state: Filters the transfers by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/transfers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "account_id": account_id,
                        "batch_id": batch_id,
                        "entity_id": entity_id,
                        "inserted_at": inserted_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "payee_account_number": payee_account_number,
                        "payee_document": payee_document,
                        "sort": sort,
                        "state": state,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=TransferListResponse,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_raw_response_wrapper(
            transfers.create,
        )
        self.list = to_raw_response_wrapper(
            transfers.list,
        )

    @cached_property
    def prepare(self) -> PrepareResourceWithRawResponse:
        return PrepareResourceWithRawResponse(self._transfers.prepare)


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_raw_response_wrapper(
            transfers.create,
        )
        self.list = async_to_raw_response_wrapper(
            transfers.list,
        )

    @cached_property
    def prepare(self) -> AsyncPrepareResourceWithRawResponse:
        return AsyncPrepareResourceWithRawResponse(self._transfers.prepare)


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_streamed_response_wrapper(
            transfers.create,
        )
        self.list = to_streamed_response_wrapper(
            transfers.list,
        )

    @cached_property
    def prepare(self) -> PrepareResourceWithStreamingResponse:
        return PrepareResourceWithStreamingResponse(self._transfers.prepare)


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_streamed_response_wrapper(
            transfers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            transfers.list,
        )

    @cached_property
    def prepare(self) -> AsyncPrepareResourceWithStreamingResponse:
        return AsyncPrepareResourceWithStreamingResponse(self._transfers.prepare)
