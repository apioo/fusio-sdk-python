"""
BackendScopeTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from backend_scope import BackendScope
from backend_scope_categories import BackendScopeCategories
from backend_scope_collection import BackendScopeCollection
from backend_scope_create import BackendScopeCreate
from backend_scope_update import BackendScopeUpdate
from common_message import CommonMessage
from common_message_exception import CommonMessageException

class BackendScopeTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def delete(self, scope_id: str) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["scope_id"] = scope_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/scope/$scope_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

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

    def update(self, scope_id: str, payload: BackendScopeUpdate) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["scope_id"] = scope_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/scope/$scope_id<[0-9]+|^~>", pathParams)

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

    def get(self, scope_id: str) -> BackendScope:
        try:
            pathParams = {}
            pathParams["scope_id"] = scope_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/scope/$scope_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendScope.from_json(response.content)

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

    def get_categories(self, ) -> BackendScopeCategories:
        try:
            pathParams = {}

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/scope/categories", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendScopeCategories.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    def create(self, payload: BackendScopeCreate) -> CommonMessage:
        try:
            pathParams = {}

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/scope", pathParams)

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

    def get_all(self, start_index: int, count: int, search: str) -> BackendScopeCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            queryStructNames = [];

            url = self.parser.url("/backend/scope", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendScopeCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


