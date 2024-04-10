"""
ConsumerTokenTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .common_message import CommonMessage
from .common_message_exception import CommonMessageException
from .consumer_token import ConsumerToken
from .consumer_token_access_token import ConsumerTokenAccessToken
from .consumer_token_collection import ConsumerTokenCollection
from .consumer_token_create import ConsumerTokenCreate
from .consumer_token_update import ConsumerTokenUpdate

class ConsumerTokenTag(sdkgen.TagAbstract):
    @classmethod
    def __init__(cls, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    @classmethod
    def delete(cls, token_id: str) -> CommonMessage:
        try:
            path_params = {}
            path_params["token_id"] = token_id

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/consumer/token/$token_id<[0-9]+|^~>", path_params)

            headers = {}

            response = cls.http_client.delete(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

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

    @classmethod
    def update(cls, token_id: str, payload: ConsumerTokenUpdate) -> ConsumerTokenAccessToken:
        try:
            path_params = {}
            path_params["token_id"] = token_id

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/consumer/token/$token_id<[0-9]+|^~>", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = cls.http_client.put(url, headers=headers, params=cls.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerTokenAccessToken.model_validate_json(json_data=response.content)

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

    @classmethod
    def get(cls, token_id: str) -> ConsumerToken:
        try:
            path_params = {}
            path_params["token_id"] = token_id

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/consumer/token/$token_id<[0-9]+|^~>", path_params)

            headers = {}

            response = cls.http_client.get(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerToken.model_validate_json(json_data=response.content)

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

    @classmethod
    def create(cls, payload: ConsumerTokenCreate) -> ConsumerTokenAccessToken:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/consumer/token", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = cls.http_client.post(url, headers=headers, params=cls.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerTokenAccessToken.model_validate_json(json_data=response.content)

            if response.status_code == 400:
                raise CommonMessageException(response.content)
            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    @classmethod
    def get_all(cls, start_index: int, count: int, search: str) -> ConsumerTokenCollection:
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = cls.parser.url("/consumer/token", path_params)

            headers = {}

            response = cls.http_client.get(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerTokenCollection.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


