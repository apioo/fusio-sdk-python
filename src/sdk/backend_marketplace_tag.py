"""
BackendMarketplaceTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .backend_marketplace_action_tag import BackendMarketplaceActionTag
from .backend_marketplace_app_tag import BackendMarketplaceAppTag

class BackendMarketplaceTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)

    def app(self) -> BackendMarketplaceAppTag:
        return BackendMarketplaceAppTag(
            self.http_client,
            self.parser
        )

    def action(self) -> BackendMarketplaceActionTag:
        return BackendMarketplaceActionTag(
            self.http_client,
            self.parser
        )


