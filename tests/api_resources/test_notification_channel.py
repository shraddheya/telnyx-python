from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestNotificationChannel(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NotificationChannel.list()
        request_mock.assert_requested("get", "/v2/notification_channels")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.NotificationChannel.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/notification_channels/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.NotificationChannel)

    @pytest.mark.skip(reason="Create mismatch")
    def test_is_creatable(self, request_mock):
        resource = telnyx.NotificationChannel.create()
        request_mock.assert_requested("post", "/v2/notification_channels")
        assert isinstance(resource, telnyx.NotificationChannel)

    @pytest.mark.skip(reason="Create mismatch")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.NotificationChannel.modify(TEST_RESOURCE_ID, name="Test")
        request_mock.assert_requested(
            "patch", "/v2/notification_channels/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.NotificationChannel)

    @pytest.mark.skip(reason="Not released, no path yet")
    def test_is_deletable(self, request_mock):
        resource = telnyx.NotificationChannel.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/notification_channels/%s" % TEST_RESOURCE_ID
        )
