"""
BackendGeneratorTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException

from .backend_generator_index_providers import BackendGeneratorIndexProviders
from .backend_generator_provider import BackendGeneratorProvider
from .backend_generator_provider_changelog import BackendGeneratorProviderChangelog
from .backend_generator_provider_config import BackendGeneratorProviderConfig
from .common_form_container import CommonFormContainer
from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class BackendGeneratorTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)

    pass


    def get_changelog(self, provider: str, payload: BackendGeneratorProviderConfig) -> BackendGeneratorProviderChangelog:
        try:
            path_params = {}
            path_params["provider"] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/generator/:provider", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return BackendGeneratorProviderChangelog.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass

    def execute_provider(self, provider: str, payload: BackendGeneratorProvider) -> CommonMessage:
        try:
            path_params = {}
            path_params["provider"] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/generator/:provider", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass

    def get_form(self, provider: str) -> CommonFormContainer:
        try:
            path_params = {}
            path_params["provider"] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/generator/:provider", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonFormContainer.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass

    def get_classes(self) -> BackendGeneratorIndexProviders:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/generator", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendGeneratorIndexProviders.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass


