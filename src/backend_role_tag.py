"""
BackendRoleTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from backend_role import BackendRole
from backend_role_collection import BackendRoleCollection
from backend_role_create import BackendRoleCreate
from backend_role_update import BackendRoleUpdate
from common_message import CommonMessage
from common_message_exception import CommonMessageException

class BackendRoleTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def delete(self, role_id: str) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["role_id"] = role_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/role/$role_id<[0-9]+|^~>", pathParams)

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

    def update(self, role_id: str, payload: BackendRoleUpdate) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["role_id"] = role_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/role/$role_id<[0-9]+|^~>", pathParams)

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

    def get(self, role_id: str) -> BackendRole:
        try:
            pathParams = {}
            pathParams["role_id"] = role_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/role/$role_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendRole.from_json(response.content)

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

    def create(self, payload: BackendRoleCreate) -> CommonMessage:
        try:
            pathParams = {}

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/role", pathParams)

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

    def get_all(self, start_index: int, count: int, search: str) -> BackendRoleCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            queryStructNames = [];

            url = self.parser.url("/backend/role", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendRoleCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


