"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .authorization_tag import AuthorizationTag
from .system_tag import SystemTag
from .consumer_tag import ConsumerTag
from .backend_tag import BackendTag

class Client(sdkgen.ClientAbstract):
    def __init__(self, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)

    def authorization(self) -> AuthorizationTag:
        return AuthorizationTag(
            self.http_client,
            self.parser
        )

    def system(self) -> SystemTag:
        return SystemTag(
            self.http_client,
            self.parser
        )

    def consumer(self) -> ConsumerTag:
        return ConsumerTag(
            self.http_client,
            self.parser
        )

    def backend(self) -> BackendTag:
        return BackendTag(
            self.http_client,
            self.parser
        )



    @staticmethod
    def build():
        return Client("https://api.sdkgen.app/", sdkgen.Anonymous())

