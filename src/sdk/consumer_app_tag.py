"""
ConsumerAppTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .common_message import CommonMessage
from .common_message_exception import CommonMessageException
from .consumer_app import ConsumerApp
from .consumer_app_collection import ConsumerAppCollection
from .consumer_app_create import ConsumerAppCreate
from .consumer_app_update import ConsumerAppUpdate

class ConsumerAppTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def create(self, payload: ConsumerAppCreate) -> CommonMessage:
        """
        Creates a new app for the authenticated user
        """
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/app', path_params)

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
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def delete(self, app_id: str) -> CommonMessage:
        """
        Deletes an existing app for the authenticated user
        """
        try:
            path_params = {}
            path_params['app_id'] = app_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/app/$app_id<[0-9]+|^~>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('DELETE', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = CommonMessage.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get(self, app_id: str) -> ConsumerApp:
        """
        Returns a specific app for the authenticated user
        """
        try:
            path_params = {}
            path_params['app_id'] = app_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/app/$app_id<[0-9]+|^~>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ConsumerApp.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_all(self, start_index: int, count: int, search: str) -> ConsumerAppCollection:
        """
        Returns a paginated list of apps which are assigned to the authenticated user
        """
        try:
            path_params = {}

            query_params = {}
            query_params['startIndex'] = start_index
            query_params['count'] = count
            query_params['search'] = search

            query_struct_names = []

            url = self.parser.url('/consumer/app', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ConsumerAppCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def update(self, app_id: str, payload: ConsumerAppUpdate) -> CommonMessage:
        """
        Updates an existing app for the authenticated user
        """
        try:
            path_params = {}
            path_params['app_id'] = app_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/app/$app_id<[0-9]+|^~>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('PUT', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = CommonMessage.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



