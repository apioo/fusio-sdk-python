"""
ConsumerAppTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from common_message import CommonMessage
from common_message_exception import CommonMessageException
from consumer_app import ConsumerApp
from consumer_app_collection import ConsumerAppCollection
from consumer_app_create import ConsumerAppCreate
from consumer_app_update import ConsumerAppUpdate

class ConsumerAppTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def delete(self, app_id: str) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["app_id"] = app_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/consumer/app/$app_id<[0-9]+|^~>", pathParams)

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

    def update(self, app_id: str, payload: ConsumerAppUpdate) -> CommonMessage:
        try:
            pathParams = {}
            pathParams["app_id"] = app_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/consumer/app/$app_id<[0-9]+|^~>", pathParams)

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

    def get(self, app_id: str) -> ConsumerApp:
        try:
            pathParams = {}
            pathParams["app_id"] = app_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/consumer/app/$app_id<[0-9]+|^~>", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerApp.from_json(response.content)

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

    def create(self, payload: ConsumerAppCreate) -> CommonMessage:
        try:
            pathParams = {}

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/consumer/app", pathParams)

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

    def get_all(self, start_index: int, count: int, search: str) -> ConsumerAppCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            queryStructNames = [];

            url = self.parser.url("/consumer/app", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerAppCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


