"""
ConsumerPaymentTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .common_message_exception import CommonMessageException
from .consumer_payment_checkout_request import ConsumerPaymentCheckoutRequest
from .consumer_payment_checkout_response import ConsumerPaymentCheckoutResponse
from .consumer_payment_portal_request import ConsumerPaymentPortalRequest
from .consumer_payment_portal_response import ConsumerPaymentPortalResponse

class ConsumerPaymentTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def checkout(self, provider: str, payload: ConsumerPaymentCheckoutRequest) -> ConsumerPaymentCheckoutResponse:
        try:
            path_params = {}
            path_params['provider'] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/payment/:provider/checkout', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('POST', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ConsumerPaymentCheckoutResponse.model_validate_json(json_data=response.content)

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

    def portal(self, provider: str, payload: ConsumerPaymentPortalRequest) -> ConsumerPaymentPortalResponse:
        try:
            path_params = {}
            path_params['provider'] = provider

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/payment/:provider/portal', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('POST', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ConsumerPaymentPortalResponse.model_validate_json(json_data=response.content)

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



