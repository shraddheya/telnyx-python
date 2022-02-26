from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    nested_resource_class_methods
)


class WhatsappBusinessAccount(
    ListableAPIResource
):
    OBJECT_NAME = "whatsapp_business_account"
