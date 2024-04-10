"""
BackendAccountTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .backend_account_change_password import BackendAccountChangePassword
from .backend_user import BackendUser
from .backend_user_update import BackendUserUpdate
from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class BackendAccountTag(sdkgen.TagAbstract):
    @classmethod
    def __init__(cls, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    @classmethod
    def change_password(cls, payload: BackendAccountChangePassword) -> CommonMessage:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/backend/account/change_password", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = cls.http_client.put(url, headers=headers, params=cls.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

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

    @classmethod
    def update(cls, payload: BackendUserUpdate) -> CommonMessage:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/backend/account", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = cls.http_client.put(url, headers=headers, params=cls.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

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

    @classmethod
    def get(cls) -> BackendUser:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/backend/account", path_params)

            headers = {}

            response = cls.http_client.get(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendUser.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


