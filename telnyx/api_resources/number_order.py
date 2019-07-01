from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)


class NumberOrder(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "number_order"
