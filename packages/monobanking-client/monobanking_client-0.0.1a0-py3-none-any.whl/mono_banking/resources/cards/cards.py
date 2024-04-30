# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from .look import (
    LookResource,
    AsyncLookResource,
    LookResourceWithRawResponse,
    AsyncLookResourceWithRawResponse,
    LookResourceWithStreamingResponse,
    AsyncLookResourceWithStreamingResponse,
)
from ...types import (
    card_list_params,
    card_create_params,
    card_update_params,
    card_activate_plastic_card_params,
)
from .prepaid import (
    PrepaidResource,
    AsyncPrepaidResource,
    PrepaidResourceWithRawResponse,
    AsyncPrepaidResourceWithRawResponse,
    PrepaidResourceWithStreamingResponse,
    AsyncPrepaidResourceWithStreamingResponse,
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
from .prepaid.prepaid import PrepaidResource, AsyncPrepaidResource
from ...types.card_list_response import CardListResponse
from ...types.card_create_response import CardCreateResponse
from ...types.card_update_response import CardUpdateResponse
from ...types.card_retrieve_response import CardRetrieveResponse
from ...types.card_activate_plastic_card_response import CardActivatePlasticCardResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def prepaid(self) -> PrepaidResource:
        return PrepaidResource(self._client)

    @cached_property
    def look(self) -> LookResource:
        return LookResource(self._client)

    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        return CardsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        cardholder: card_create_params.Cardholder,
        configuration_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_balance: Optional[card_create_params.InitialBalance] | NotGiven = NOT_GIVEN,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCreateResponse:
        """
        You can use this endpoint to create cards

        Args:
          account_id: Account ID

          cardholder: Represents the cardholder information

          configuration_group_id: Card configuration group ID.

              By default, if the configuration group ID is not specified, it is taken from the
              client's default configuration.

          initial_balance: The current amount available or the balance

          nickname: Card nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "cardholder": cardholder,
                    "configuration_group_id": configuration_group_id,
                    "initial_balance": initial_balance,
                    "nickname": nickname,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
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
    ) -> CardRetrieveResponse:
        """
        Gets card data with sensitive information

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
            f"/v1/cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardRetrieveResponse,
        )

    def update(
        self,
        card_id: str,
        *,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        spending_control_id: Optional[str] | NotGiven = NOT_GIVEN,
        state: Literal["active", "frozen", "canceled", "created"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardUpdateResponse:
        """
        You can use this endpoint to update cards

        Args:
          card_id: Indicates the format for resource's ID

          nickname: Card nickname

          spending_control_id: Spending control ID

          state: State of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            f"/v1/cards/{card_id}",
            body=maybe_transform(
                {
                    "nickname": nickname,
                    "spending_control_id": spending_control_id,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: Union[List[str], str] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Union[
            List[Literal["active", "frozen", "canceled", "created"]], Literal["active", "frozen", "canceled", "created"]
        ]
        | NotGiven = NOT_GIVEN,
        type: Literal["virtual", "plastic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardListResponse:
        """List cards.

        the result will include the cards with the paging information

        Args:
          account_id: Filter by one or many account IDs.

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filter by one or many account IDs.

          type: Filter by one or many account IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                        "type": type,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )

    def activate_plastic_card(
        self,
        *,
        account_id: str,
        cardholder_id: str,
        configuration_group_id: str,
        spending_control_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardActivatePlasticCardResponse:
        """
        Activate a plastic card

        Args:
          account_id: Account ID

          cardholder_id: Cardholder ID

          configuration_group_id: Card Config Group ID

          spending_control_id: Spending Control ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/cards/activate_plastic_card",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "cardholder_id": cardholder_id,
                    "configuration_group_id": configuration_group_id,
                    "spending_control_id": spending_control_id,
                },
                card_activate_plastic_card_params.CardActivatePlasticCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardActivatePlasticCardResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def prepaid(self) -> AsyncPrepaidResource:
        return AsyncPrepaidResource(self._client)

    @cached_property
    def look(self) -> AsyncLookResource:
        return AsyncLookResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        return AsyncCardsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        cardholder: card_create_params.Cardholder,
        configuration_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_balance: Optional[card_create_params.InitialBalance] | NotGiven = NOT_GIVEN,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCreateResponse:
        """
        You can use this endpoint to create cards

        Args:
          account_id: Account ID

          cardholder: Represents the cardholder information

          configuration_group_id: Card configuration group ID.

              By default, if the configuration group ID is not specified, it is taken from the
              client's default configuration.

          initial_balance: The current amount available or the balance

          nickname: Card nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/cards",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "cardholder": cardholder,
                    "configuration_group_id": configuration_group_id,
                    "initial_balance": initial_balance,
                    "nickname": nickname,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
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
    ) -> CardRetrieveResponse:
        """
        Gets card data with sensitive information

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
            f"/v1/cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardRetrieveResponse,
        )

    async def update(
        self,
        card_id: str,
        *,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        spending_control_id: Optional[str] | NotGiven = NOT_GIVEN,
        state: Literal["active", "frozen", "canceled", "created"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardUpdateResponse:
        """
        You can use this endpoint to update cards

        Args:
          card_id: Indicates the format for resource's ID

          nickname: Card nickname

          spending_control_id: Spending control ID

          state: State of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            f"/v1/cards/{card_id}",
            body=await async_maybe_transform(
                {
                    "nickname": nickname,
                    "spending_control_id": spending_control_id,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardUpdateResponse,
        )

    async def list(
        self,
        *,
        account_id: Union[List[str], str] | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        state: Union[
            List[Literal["active", "frozen", "canceled", "created"]], Literal["active", "frozen", "canceled", "created"]
        ]
        | NotGiven = NOT_GIVEN,
        type: Literal["virtual", "plastic"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardListResponse:
        """List cards.

        the result will include the cards with the paging information

        Args:
          account_id: Filter by one or many account IDs.

          page_number: Number of the page

          page_size: Amount of registers that must be listed by page

          state: Filter by one or many account IDs.

          type: Filter by one or many account IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "state": state,
                        "type": type,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )

    async def activate_plastic_card(
        self,
        *,
        account_id: str,
        cardholder_id: str,
        configuration_group_id: str,
        spending_control_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardActivatePlasticCardResponse:
        """
        Activate a plastic card

        Args:
          account_id: Account ID

          cardholder_id: Cardholder ID

          configuration_group_id: Card Config Group ID

          spending_control_id: Spending Control ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/cards/activate_plastic_card",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "cardholder_id": cardholder_id,
                    "configuration_group_id": configuration_group_id,
                    "spending_control_id": spending_control_id,
                },
                card_activate_plastic_card_params.CardActivatePlasticCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardActivatePlasticCardResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )
        self.activate_plastic_card = to_raw_response_wrapper(
            cards.activate_plastic_card,
        )

    @cached_property
    def prepaid(self) -> PrepaidResourceWithRawResponse:
        return PrepaidResourceWithRawResponse(self._cards.prepaid)

    @cached_property
    def look(self) -> LookResourceWithRawResponse:
        return LookResourceWithRawResponse(self._cards.look)


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )
        self.activate_plastic_card = async_to_raw_response_wrapper(
            cards.activate_plastic_card,
        )

    @cached_property
    def prepaid(self) -> AsyncPrepaidResourceWithRawResponse:
        return AsyncPrepaidResourceWithRawResponse(self._cards.prepaid)

    @cached_property
    def look(self) -> AsyncLookResourceWithRawResponse:
        return AsyncLookResourceWithRawResponse(self._cards.look)


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )
        self.activate_plastic_card = to_streamed_response_wrapper(
            cards.activate_plastic_card,
        )

    @cached_property
    def prepaid(self) -> PrepaidResourceWithStreamingResponse:
        return PrepaidResourceWithStreamingResponse(self._cards.prepaid)

    @cached_property
    def look(self) -> LookResourceWithStreamingResponse:
        return LookResourceWithStreamingResponse(self._cards.look)


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
        self.activate_plastic_card = async_to_streamed_response_wrapper(
            cards.activate_plastic_card,
        )

    @cached_property
    def prepaid(self) -> AsyncPrepaidResourceWithStreamingResponse:
        return AsyncPrepaidResourceWithStreamingResponse(self._cards.prepaid)

    @cached_property
    def look(self) -> AsyncLookResourceWithStreamingResponse:
        return AsyncLookResourceWithStreamingResponse(self._cards.look)
