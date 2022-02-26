from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestShortCode(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.ShortCode.list()
        request_mock.assert_requested("get", "/v2/short_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.ShortCode)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.ShortCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/short_codes/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.ShortCode)

    def test_is_saveable(self, request_mock):
        short_code = telnyx.ShortCode.retrieve(TEST_RESOURCE_ID)
        short_code.messaging_profile_id = "2"
        resource = short_code.save()
        request_mock.assert_requested("patch", "/v2/short_codes/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.ShortCode)
        assert resource is short_code

    def test_is_modifiable(self, request_mock):
        resource = telnyx.ShortCode.modify(TEST_RESOURCE_ID, messaging_profile_id="2")
        request_mock.assert_requested("patch", "/v2/short_codes/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.ShortCode)
