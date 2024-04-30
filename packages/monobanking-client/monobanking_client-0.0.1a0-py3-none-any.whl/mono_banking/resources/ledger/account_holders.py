# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...types.ledger import account_holder_create_params, account_holder_update_state_params
from ...types.ledger.account_holder_create_response import AccountHolderCreateResponse
from ...types.ledger.account_holder_retrieve_response import AccountHolderRetrieveResponse
from ...types.ledger.account_holder_update_state_response import AccountHolderUpdateStateResponse

__all__ = ["AccountHoldersResource", "AsyncAccountHoldersResource"]


class AccountHoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountHoldersResourceWithRawResponse:
        return AccountHoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountHoldersResourceWithStreamingResponse:
        return AccountHoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: account_holder_create_params.Address,
        external_id: Optional[str],
        person: account_holder_create_params.Person,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Creates a new third-party account holder and associates it to the tenant.

        Args:
          address: Contains the address information related to the account holder.

          external_id: Represents a unique external_id generated and provided by the API user. The API
              user is responsible to generate and provide a unique id for all their
              organization's account holders.

          person: Contains the specific person information of the account holder.

          email: Account holder's email

          metadata: Contains additional information that provide context, description, or
              supplementary details about the data being transmitted.

          phone_number: Account holder's phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ledger/account_holders",
            body=maybe_transform(
                {
                    "address": address,
                    "external_id": external_id,
                    "person": person,
                    "email": email,
                    "metadata": metadata,
                    "phone_number": phone_number,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderCreateResponse,
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
    ) -> AccountHolderRetrieveResponse:
        """
        Get detailed information about an account holder by ID.

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
            f"/v1/ledger/account_holders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderRetrieveResponse,
        )

    def update_state(
        self,
        id: str,
        *,
        state: Literal["active", "blocked"],
        detail: str | NotGiven = NOT_GIVEN,
        reason: Literal["fraud", "user_request", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateStateResponse:
        """
        Updates state of an third-party account holder to `active` or `blocked`

        Args:
          id: Indicates the format for resource's ID

          state: It represents the current state of the account holder, and these are the
              possible states of an account holder:

              - active: it is enable to manage and perform actions with its accounts.
              - blocked: it is blocked by the client, but you could also make it active again.

          detail: It provides a textual reason why the account holder is blocked in case of the
              state_reason value is `other`.

          reason: It provides the reason why the account holder could be blocked. It is required
              when the account holder is transitioned to being blocked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/ledger/account_holders/{id}",
            body=maybe_transform(
                {
                    "state": state,
                    "detail": detail,
                    "reason": reason,
                },
                account_holder_update_state_params.AccountHolderUpdateStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderUpdateStateResponse,
        )


class AsyncAccountHoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountHoldersResourceWithRawResponse:
        return AsyncAccountHoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountHoldersResourceWithStreamingResponse:
        return AsyncAccountHoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: account_holder_create_params.Address,
        external_id: Optional[str],
        person: account_holder_create_params.Person,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Creates a new third-party account holder and associates it to the tenant.

        Args:
          address: Contains the address information related to the account holder.

          external_id: Represents a unique external_id generated and provided by the API user. The API
              user is responsible to generate and provide a unique id for all their
              organization's account holders.

          person: Contains the specific person information of the account holder.

          email: Account holder's email

          metadata: Contains additional information that provide context, description, or
              supplementary details about the data being transmitted.

          phone_number: Account holder's phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ledger/account_holders",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "external_id": external_id,
                    "person": person,
                    "email": email,
                    "metadata": metadata,
                    "phone_number": phone_number,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderCreateResponse,
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
    ) -> AccountHolderRetrieveResponse:
        """
        Get detailed information about an account holder by ID.

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
            f"/v1/ledger/account_holders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderRetrieveResponse,
        )

    async def update_state(
        self,
        id: str,
        *,
        state: Literal["active", "blocked"],
        detail: str | NotGiven = NOT_GIVEN,
        reason: Literal["fraud", "user_request", "other"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateStateResponse:
        """
        Updates state of an third-party account holder to `active` or `blocked`

        Args:
          id: Indicates the format for resource's ID

          state: It represents the current state of the account holder, and these are the
              possible states of an account holder:

              - active: it is enable to manage and perform actions with its accounts.
              - blocked: it is blocked by the client, but you could also make it active again.

          detail: It provides a textual reason why the account holder is blocked in case of the
              state_reason value is `other`.

          reason: It provides the reason why the account holder could be blocked. It is required
              when the account holder is transitioned to being blocked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/ledger/account_holders/{id}",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "detail": detail,
                    "reason": reason,
                },
                account_holder_update_state_params.AccountHolderUpdateStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderUpdateStateResponse,
        )


class AccountHoldersResourceWithRawResponse:
    def __init__(self, account_holders: AccountHoldersResource) -> None:
        self._account_holders = account_holders

        self.create = to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update_state = to_raw_response_wrapper(
            account_holders.update_state,
        )


class AsyncAccountHoldersResourceWithRawResponse:
    def __init__(self, account_holders: AsyncAccountHoldersResource) -> None:
        self._account_holders = account_holders

        self.create = async_to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update_state = async_to_raw_response_wrapper(
            account_holders.update_state,
        )


class AccountHoldersResourceWithStreamingResponse:
    def __init__(self, account_holders: AccountHoldersResource) -> None:
        self._account_holders = account_holders

        self.create = to_streamed_response_wrapper(
            account_holders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_holders.retrieve,
        )
        self.update_state = to_streamed_response_wrapper(
            account_holders.update_state,
        )


class AsyncAccountHoldersResourceWithStreamingResponse:
    def __init__(self, account_holders: AsyncAccountHoldersResource) -> None:
        self._account_holders = account_holders

        self.create = async_to_streamed_response_wrapper(
            account_holders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_holders.retrieve,
        )
        self.update_state = async_to_streamed_response_wrapper(
            account_holders.update_state,
        )
