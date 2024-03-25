"""
BackendSchemaTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from backend_schema import BackendSchema
from backend_schema_collection import BackendSchemaCollection
from backend_schema_create import BackendSchemaCreate
from backend_schema_form import BackendSchemaForm
from backend_schema_preview_response import BackendSchemaPreviewResponse
from backend_schema_update import BackendSchemaUpdate
from common_message import CommonMessage
from common_message_exception import CommonMessageException

class BackendSchemaTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def delete(self, schema_id: str) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["schema_id"] = schema_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 404:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 410:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def update(self, schema_id: str, payload: BackendSchemaUpdate) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["schema_id"] = schema_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=this.parser.query(queryParams, queryStructNames), data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.from_json(response.content)

            if response.status_code == 400:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 404:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 410:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def get(self, schema_id: str) -> BackendSchema:
        try:
            pathParams = {}
            pathParams["schema_id"] = schema_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema/$schema_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchema.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 404:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 410:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def update_form(self, schema_id: str, payload: BackendSchemaForm) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["schema_id"] = schema_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema/form/$schema_id<[0-9]+>", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=this.parser.query(queryParams, queryStructNames), data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.from_json(response.content)

            if response.status_code == 400:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 404:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 410:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def get_preview(self, schema_id: str) -> BackendSchemaPreviewResponse:
        try:
            pathParams = {}
            pathParams["schema_id"] = schema_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema/preview/:schema_id", pathParams)

            headers = {}

            response = self.http_client.post(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchemaPreviewResponse.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def create(self, payload: BackendSchemaCreate) -> CommonMessage:
        try:
            pathParams = {}

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/schema", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=this.parser.query(queryParams, queryStructNames), data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.from_json(response.content)

            if response.status_code == 400:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def get_all(self, start_index: int, count: int, search: str) -> BackendSchemaCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            queryStructNames = [];

            url = self.parser.url("/backend/schema", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendSchemaCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

