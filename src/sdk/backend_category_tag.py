"""
BackendCategoryTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .backend_category import BackendCategory
from .backend_category_collection import BackendCategoryCollection
from .backend_category_create import BackendCategoryCreate
from .backend_category_update import BackendCategoryUpdate
from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class BackendCategoryTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def delete(self, category_id: str) -> CommonMessage:
        try:
            path_params = {}
            path_params['category_id'] = category_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/category/$category_id<[0-9]+|^~>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('DELETE', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = CommonMessage.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 404:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 410:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def update(self, category_id: str, payload: BackendCategoryUpdate) -> CommonMessage:
        try:
            path_params = {}
            path_params['category_id'] = category_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/category/$category_id<[0-9]+|^~>', path_params)

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
            if statusCode == 400:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 404:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 410:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get(self, category_id: str) -> BackendCategory:
        try:
            path_params = {}
            path_params['category_id'] = category_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/category/$category_id<[0-9]+|^~>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendCategory.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode == 401:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 404:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 410:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            if statusCode == 500:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def create(self, payload: BackendCategoryCreate) -> CommonMessage:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/category', path_params)

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

    def get_all(self, start_index: int, count: int, search: str) -> BackendCategoryCollection:
        try:
            path_params = {}

            query_params = {}
            query_params['startIndex'] = start_index
            query_params['count'] = count
            query_params['search'] = search

            query_struct_names = []

            url = self.parser.url('/backend/category', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendCategoryCollection.model_validate_json(json_data=response.content)

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



