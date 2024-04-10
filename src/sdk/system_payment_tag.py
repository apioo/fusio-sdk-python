"""
SystemPaymentTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class SystemPaymentTag(sdkgen.TagAbstract):
    @classmethod
    def __init__(cls, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    @classmethod
    def webhook(cls, provider: str) -> CommonMessage:
        try:
            path_params = {}
            path_params["provider"] = provider

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/system/payment/:provider/webhook", path_params)

            headers = {}

            response = cls.http_client.post(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return CommonMessage.model_validate_json(json_data=response.content)

            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


