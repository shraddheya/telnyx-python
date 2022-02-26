from __future__ import absolute_import, division, print_function

import pytest

import telnyx

NUMBER_RESERVATION_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


def create_number_reservation():
    return telnyx.NumberReservation.create(
        phone_numbers=[{"phone_number": "++19705555098"}]
    )


class TestNumberReservation(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NumberReservation.list()
        request_mock.assert_requested("get", "/v2/number_reservations")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.NumberReservation)

    def test_is_retrievable(self, request_mock):
        resources = telnyx.NumberReservation.retrieve(NUMBER_RESERVATION_ID)
        request_mock.assert_requested(
            "get", "/v2/number_reservations/{}".format(NUMBER_RESERVATION_ID)
        )
        assert isinstance(resources, telnyx.NumberReservation)

    def test_is_creatable(self, request_mock):
        resource = create_number_reservation()
        request_mock.assert_requested("post", "/v2/number_reservations")
        assert isinstance(resource, telnyx.NumberReservation)

    @pytest.mark.skip(reason="async, wait for response")
    def test_can_call_extend(self, request_mock):
        resource = create_number_reservation()
        resource.extend()
        request_mock.assert_requested(
            "post", "/v2/number_reservations/%s/actions/extend" % NUMBER_RESERVATION_ID
        )
        assert isinstance(resource, telnyx.NumberReservation)

    @pytest.mark.skip(reason="async, wait for response")
    def test_can_call_reservation_extend(self, request_mock):
        resource = create_number_reservation()
        resource.create_extend(NUMBER_RESERVATION_ID)
        request_mock.assert_requested(
            "post", "/v2/number_reservations/%s/actions/extend" % NUMBER_RESERVATION_ID
        )
        assert isinstance(resource, telnyx.NumberReservation)
