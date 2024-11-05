"""
BackendGeneratorTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

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


    def get_changelog(self, provider: str, payload: BackendGeneratorProviderConfig) -> BackendGeneratorProviderChangelog:
        try:
            path_params = {}
            path_params['provider'] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/generator/:provider', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('PUT', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendGeneratorProviderChangelog.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 400:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def execute_provider(self, provider: str, payload: BackendGeneratorProvider) -> CommonMessage:
        try:
            path_params = {}
            path_params['provider'] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/generator/:provider', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('POST', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = CommonMessage.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 400:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_form(self, provider: str) -> CommonFormContainer:
        try:
            path_params = {}
            path_params['provider'] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/generator/:provider', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = CommonFormContainer.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 400:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_classes(self) -> BackendGeneratorIndexProviders:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/generator', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendGeneratorIndexProviders.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



