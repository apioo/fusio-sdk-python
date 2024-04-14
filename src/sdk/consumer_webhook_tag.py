"""
ConsumerWebhookTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .common_message import CommonMessage
from .common_message_exception import CommonMessageException
from .consumer_webhook import ConsumerWebhook
from .consumer_webhook_collection import ConsumerWebhookCollection
from .consumer_webhook_create import ConsumerWebhookCreate
from .consumer_webhook_update import ConsumerWebhookUpdate

class ConsumerWebhookTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def delete(self, webhook_id: str) -> CommonMessage:
        try:
            path_params = {}
            path_params["webhook_id"] = webhook_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/webhook/$webhook_id<[0-9]+|^~>", path_params)

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

    def update(self, webhook_id: str, payload: ConsumerWebhookUpdate) -> CommonMessage:
        try:
            path_params = {}
            path_params["webhook_id"] = webhook_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/webhook/$webhook_id<[0-9]+|^~>", path_params)

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

    def get(self, webhook_id: str) -> ConsumerWebhook:
        try:
            path_params = {}
            path_params["webhook_id"] = webhook_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/webhook/$webhook_id<[0-9]+|^~>", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerWebhook.model_validate_json(json_data=response.content)

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

    def create(self, payload: ConsumerWebhookCreate) -> CommonMessage:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/webhook", path_params)

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

    def get_all(self, start_index: int, count: int, search: str) -> ConsumerWebhookCollection:
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/consumer/webhook", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerWebhookCollection.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


