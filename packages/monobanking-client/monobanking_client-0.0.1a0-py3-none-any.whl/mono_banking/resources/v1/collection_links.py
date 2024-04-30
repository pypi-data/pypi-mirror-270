# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.v1 import collection_link_list_params, collection_link_create_params
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
from ...types.v1.collection_link_list_response import CollectionLinkListResponse
from ...types.v1.collection_link_create_response import CollectionLinkCreateResponse
from ...types.v1.collection_link_retrieve_response import CollectionLinkRetrieveResponse

__all__ = ["CollectionLinksResource", "AsyncCollectionLinksResource"]


class CollectionLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionLinksResourceWithRawResponse:
        return CollectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionLinksResourceWithStreamingResponse:
        return CollectionLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: collection_link_create_params.Amount,
        amount_validation: Literal["free", "fixed", "can_be_less", "can_be_greater"],
        usage_type: Literal["single_use", "multi_use"],
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        payer: collection_link_create_params.Payer | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        reference: collection_link_create_params.Reference | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkCreateResponse:
        """
        This endpoint allows you to create a collection link to share it with anybody.

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          amount_validation: Sets the collection link validations of the `amount` field. Two validations will
              always be present in the checkout form `amount` field:

              1. The amount must be greater than zero.
              2. The amount must be within the limits allowed by Mono.

              The field "amount_validation" is an additional validation configured to be
              applied to the checkout form's amount field.

              - fixed: No validation will be applied to the amount field in the checkout form,
                and the user will not be able to enter an amount. The checkout form's amount
                field will contain the configured amount (the amount is fixed).
              - free: No validation will be applied, and the user can enter any amount in the
                checkout form.
              - can_be_less: The amount entered by the user can be less than or equal to the
                configured amount.
              - can_be_greater: The amount entered by the user can be greater than or equal to
                the configured amount.

          usage_type:
              Sets the collection link type. There are two types of collection links:

              1. single_use: As the name suggests, this type of collection link can only be
                 used once. When a successful payment is made, the link will be disabled. The
                 collection link will display a message if a user tries to access it again
                 after the payment has been made.
              2. multi_use: As the name suggests, this type of collection link can be used
                 multiple times

          expires_at: Sets an expiration date and time for the collection link. If a user attempts to
              enter an expired link, a message will be displayed informing them that the link
              has expired.

          external_id: Associates the collection link with an external register. For example, this
              field may contain identifiers of entities that could be used in some external
              system.

          payer: Sets the payer data, which will be preloaded into the checkout form. This payer
              data can be optional

          redirect_url: Sets a URL on the redirect button on the payment receipt after payment is made.
              The URL contains three parameters from the query string:

              1. id: this contains the same value as the field "external_id"
              2. clink_id: this is the collection link ID
              3. intent_id: this is the collection intent ID or the payment ID

          reference: Sets the reference field in the checkout form. When there is no reference, and
              it is configured not to be editable, the checkout form reference field will not
              be visible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/collection_links",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "amount_validation": amount_validation,
                    "usage_type": usage_type,
                    "expires_at": expires_at,
                    "external_id": external_id,
                    "payer": payer,
                    "redirect_url": redirect_url,
                    "reference": reference,
                },
                collection_link_create_params.CollectionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionLinkCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkRetrieveResponse:
        """
        This endpoint allows you to get a collection link by ID

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/collection_links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionLinkRetrieveResponse,
        )

    def list(
        self,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        expires_at: collection_link_list_params.ExpiresAt | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inserted_at: collection_link_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payer: collection_link_list_params.Payer | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        sort: collection_link_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkListResponse:
        """
        This endpoint allows you to list the created collection links

        Args:
          enabled: Filter by enabled field

          expires_at: Filter by expires_at field, it works as with range of date/time.

          external_id: Filter by external id field

          inserted_at: Filter by a range of date/time

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          payer: Filter by payer info

          reference: Filter by reference field, it works as not exact filter and must be sent 4
              characters at least.

          sort: Sorts the collection links according to the types and fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/collection_links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "expires_at": expires_at,
                        "external_id": external_id,
                        "inserted_at": inserted_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "payer": payer,
                        "reference": reference,
                        "sort": sort,
                    },
                    collection_link_list_params.CollectionLinkListParams,
                ),
            ),
            cast_to=CollectionLinkListResponse,
        )


class AsyncCollectionLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionLinksResourceWithRawResponse:
        return AsyncCollectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionLinksResourceWithStreamingResponse:
        return AsyncCollectionLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: collection_link_create_params.Amount,
        amount_validation: Literal["free", "fixed", "can_be_less", "can_be_greater"],
        usage_type: Literal["single_use", "multi_use"],
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        payer: collection_link_create_params.Payer | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        reference: collection_link_create_params.Reference | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkCreateResponse:
        """
        This endpoint allows you to create a collection link to share it with anybody.

        Args:
          account_id: Indicates the format for resource's ID

          amount: Money schema

          amount_validation: Sets the collection link validations of the `amount` field. Two validations will
              always be present in the checkout form `amount` field:

              1. The amount must be greater than zero.
              2. The amount must be within the limits allowed by Mono.

              The field "amount_validation" is an additional validation configured to be
              applied to the checkout form's amount field.

              - fixed: No validation will be applied to the amount field in the checkout form,
                and the user will not be able to enter an amount. The checkout form's amount
                field will contain the configured amount (the amount is fixed).
              - free: No validation will be applied, and the user can enter any amount in the
                checkout form.
              - can_be_less: The amount entered by the user can be less than or equal to the
                configured amount.
              - can_be_greater: The amount entered by the user can be greater than or equal to
                the configured amount.

          usage_type:
              Sets the collection link type. There are two types of collection links:

              1. single_use: As the name suggests, this type of collection link can only be
                 used once. When a successful payment is made, the link will be disabled. The
                 collection link will display a message if a user tries to access it again
                 after the payment has been made.
              2. multi_use: As the name suggests, this type of collection link can be used
                 multiple times

          expires_at: Sets an expiration date and time for the collection link. If a user attempts to
              enter an expired link, a message will be displayed informing them that the link
              has expired.

          external_id: Associates the collection link with an external register. For example, this
              field may contain identifiers of entities that could be used in some external
              system.

          payer: Sets the payer data, which will be preloaded into the checkout form. This payer
              data can be optional

          redirect_url: Sets a URL on the redirect button on the payment receipt after payment is made.
              The URL contains three parameters from the query string:

              1. id: this contains the same value as the field "external_id"
              2. clink_id: this is the collection link ID
              3. intent_id: this is the collection intent ID or the payment ID

          reference: Sets the reference field in the checkout form. When there is no reference, and
              it is configured not to be editable, the checkout form reference field will not
              be visible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/collection_links",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "amount_validation": amount_validation,
                    "usage_type": usage_type,
                    "expires_at": expires_at,
                    "external_id": external_id,
                    "payer": payer,
                    "redirect_url": redirect_url,
                    "reference": reference,
                },
                collection_link_create_params.CollectionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionLinkCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkRetrieveResponse:
        """
        This endpoint allows you to get a collection link by ID

        Args:
          id: Indicates the format for resource's ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/collection_links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionLinkRetrieveResponse,
        )

    async def list(
        self,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        expires_at: collection_link_list_params.ExpiresAt | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inserted_at: collection_link_list_params.InsertedAt | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payer: collection_link_list_params.Payer | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        sort: collection_link_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionLinkListResponse:
        """
        This endpoint allows you to list the created collection links

        Args:
          enabled: Filter by enabled field

          expires_at: Filter by expires_at field, it works as with range of date/time.

          external_id: Filter by external id field

          inserted_at: Filter by a range of date/time

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          payer: Filter by payer info

          reference: Filter by reference field, it works as not exact filter and must be sent 4
              characters at least.

          sort: Sorts the collection links according to the types and fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/collection_links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "enabled": enabled,
                        "expires_at": expires_at,
                        "external_id": external_id,
                        "inserted_at": inserted_at,
                        "page_number": page_number,
                        "page_size": page_size,
                        "payer": payer,
                        "reference": reference,
                        "sort": sort,
                    },
                    collection_link_list_params.CollectionLinkListParams,
                ),
            ),
            cast_to=CollectionLinkListResponse,
        )


class CollectionLinksResourceWithRawResponse:
    def __init__(self, collection_links: CollectionLinksResource) -> None:
        self._collection_links = collection_links

        self.create = to_raw_response_wrapper(
            collection_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collection_links.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collection_links.list,
        )


class AsyncCollectionLinksResourceWithRawResponse:
    def __init__(self, collection_links: AsyncCollectionLinksResource) -> None:
        self._collection_links = collection_links

        self.create = async_to_raw_response_wrapper(
            collection_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collection_links.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collection_links.list,
        )


class CollectionLinksResourceWithStreamingResponse:
    def __init__(self, collection_links: CollectionLinksResource) -> None:
        self._collection_links = collection_links

        self.create = to_streamed_response_wrapper(
            collection_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collection_links.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collection_links.list,
        )


class AsyncCollectionLinksResourceWithStreamingResponse:
    def __init__(self, collection_links: AsyncCollectionLinksResource) -> None:
        self._collection_links = collection_links

        self.create = async_to_streamed_response_wrapper(
            collection_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collection_links.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collection_links.list,
        )
