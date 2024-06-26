"""
BackendSchemaTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .backend_schema import BackendSchema
from .backend_schema_collection import BackendSchemaCollection
from .backend_schema_create import BackendSchemaCreate
from .backend_schema_form import BackendSchemaForm
from .backend_schema_preview_response import BackendSchemaPreviewResponse
from .backend_schema_update import BackendSchemaUpdate
from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class BackendSchemaTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def delete(self, schema_id: str) -> CommonMessage:
        try:
            path_params = {}
            path_params["schema_id"] = schema_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 404:
                raise CommonMessageException(response.content)
            if response.status_code == 410:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update(self, schema_id: str, payload: BackendSchemaUpdate) -> CommonMessage:
        try:
            path_params = {}
            path_params["schema_id"] = schema_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise CommonMessageException(response.content)
            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 404:
                raise CommonMessageException(response.content)
            if response.status_code == 410:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, schema_id: str) -> BackendSchema:
        try:
            path_params = {}
            path_params["schema_id"] = schema_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchema.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 404:
                raise CommonMessageException(response.content)
            if response.status_code == 410:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update_form(self, schema_id: str, payload: BackendSchemaForm) -> CommonMessage:
        try:
            path_params = {}
            path_params["schema_id"] = schema_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema/form/$schema_id<[0-9]+>", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise CommonMessageException(response.content)
            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 404:
                raise CommonMessageException(response.content)
            if response.status_code == 410:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get_preview(self, schema_id: str) -> BackendSchemaPreviewResponse:
        try:
            path_params = {}
            path_params["schema_id"] = schema_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema/preview/:schema_id", path_params)

            headers = {}

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchemaPreviewResponse.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create(self, payload: BackendSchemaCreate) -> CommonMessage:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/backend/schema", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise CommonMessageException(response.content)
            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get_all(self, start_index: int, count: int, search: str) -> BackendSchemaCollection:
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/backend/schema", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchemaCollection.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


