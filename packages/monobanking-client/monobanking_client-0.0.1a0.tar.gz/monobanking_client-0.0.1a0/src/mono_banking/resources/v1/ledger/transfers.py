# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.v1.ledger import transfer_create_params
from ....types.v1.ledger.transfer_create_response import TransferCreateResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: transfer_create_params.Amount,
        external_id: str,
        payer_account_id: str,
        receiving_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferCreateResponse:
        """Transfer funds smoothly between any two of your subaccounts

        Considerations:

        1.

        This endpoint could be only used for accounts with type `subaccount`.
        2. Both payer and receiving account should be `active`.
        3. The associated account holders should also be `active`.
        4. You can only make operations if the currency code of the payer account is the
           same as the currency code of the receiving account.
        5. You can only make operations if the currency code of the amount is the same
           as the currency code of both payer and receiving account.

        Args:
          amount: Money schema

          external_id: Unique identifier of the transfer operation

          payer_account_id: Indicates the format for resource's ID

          receiving_account_id: Indicates the format for resource's ID

          description: String field

          reference: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ledger/transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "external_id": external_id,
                    "payer_account_id": payer_account_id,
                    "receiving_account_id": receiving_account_id,
                    "description": description,
                    "reference": reference,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferCreateResponse,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: transfer_create_params.Amount,
        external_id: str,
        payer_account_id: str,
        receiving_account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        reference: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransferCreateResponse:
        """Transfer funds smoothly between any two of your subaccounts

        Considerations:

        1.

        This endpoint could be only used for accounts with type `subaccount`.
        2. Both payer and receiving account should be `active`.
        3. The associated account holders should also be `active`.
        4. You can only make operations if the currency code of the payer account is the
           same as the currency code of the receiving account.
        5. You can only make operations if the currency code of the amount is the same
           as the currency code of both payer and receiving account.

        Args:
          amount: Money schema

          external_id: Unique identifier of the transfer operation

          payer_account_id: Indicates the format for resource's ID

          receiving_account_id: Indicates the format for resource's ID

          description: String field

          reference: String field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ledger/transfers",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "external_id": external_id,
                    "payer_account_id": payer_account_id,
                    "receiving_account_id": receiving_account_id,
                    "description": description,
                    "reference": reference,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferCreateResponse,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_raw_response_wrapper(
            transfers.create,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_raw_response_wrapper(
            transfers.create,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_streamed_response_wrapper(
            transfers.create,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_streamed_response_wrapper(
            transfers.create,
        )
