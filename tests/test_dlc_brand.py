import telnyx
class TestDlcBrand(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.DLCBrand.list()
        request_mock.assert_requested("get", "/10dlc/brand")
        assert isinstance(resources.data.records, list)
        assert isinstance(resources.data.records[0], telnyx.DLCBrand)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.DLCBrand.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/10dlc/brand/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.DLCBrand)

    def test_is_creatable(self, request_mock):
        resource = telnyx.DLCBrand.create(
                isReseller = false,
                country = "US",
                companyName = "Example Company",
                displayName = "Example Company",
                entityType = "PRIVATE_PROFIT",
                vertical = "COMMUNICATION",
                ein = "142536893",
                website = "www.examplecompany.com",
                street = "123 Example St.",
                city = "Chicago",
                state = "IL",
                postalCode = "60654",
                email = "examplename@examplecompany.com",
                phone = "+13259390512",
        )
        request_mock.assert_requested("post", "/10dlc/brand")
        assert isinstance(resource, telnyx.DLCBrand)

    def test_is_saveable(self, request_mock):
        dlc_brand = telnyx.DLCBrand.retrieve(TEST_RESOURCE_ID)
        dcl_brand.isReseller = false
        dcl_brand.country = "US"
        dcl_brand.companyName = "Example Company"
        dcl_brand.displayName = "Example Company"
        dcl_brand.entityType = "PRIVATE_PROFIT"
        dcl_brand.vertical = "COMMUNICATION"
        dcl_brand.ein = "142536893"
        dcl_brand.website = "www.examplecompany.com"
        dcl_brand.street = "123 Example St."
        dcl_brand.city = "Chicago"
        dcl_brand.state = "IL"
        dcl_brand.postalCode = "60654"
        dcl_brand.email = "examplename@examplecompany.com"
        dcl_brand.phone = "+13259390512"
        resource = dlc_brand.save()
        request_mock.assert_requested(
            "patch", "/10dlc/brand/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.DLCBrand)
        assert resource is dlc_brand

    def test_is_modifiable(self, request_mock):
        resource = telnyx.DLCBrand.modify(
            TEST_RESOURCE_ID,
            isReseller = false,
            country = "US",
            companyName = "Example Company",
            displayName = "Example Company",
            entityType = "PRIVATE_PROFIT",
            vertical = "COMMUNICATION",
            ein = "142536893",
            website = "www.examplecompany.com",
            street = "123 Example St.",
            city = "Chicago",
            state = "IL",
            postalCode = "60654",
            email = "examplename@examplecompany.com",
            phone = "+13259390512",
        )
        request_mock.assert_requested(
            "patch", "/10dlc/brand/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.DLCBrand)

    def test_is_deletable(self, request_mock):
        resource = telnyx.DLCBrand.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/10dlc/brand/%s" % TEST_RESOURCE_ID
        )
