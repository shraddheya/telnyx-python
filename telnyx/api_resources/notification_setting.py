from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource
)


class NotificationSetting(
    ListableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource
):
    OBJECT_NAME = "notification_setting"
