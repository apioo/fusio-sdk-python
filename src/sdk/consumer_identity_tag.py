"""
ConsumerIdentityTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .common_message import CommonMessage
from .common_message_exception import CommonMessageException
from .consumer_identity_collection import ConsumerIdentityCollection
from .passthru import Passthru

class ConsumerIdentityTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def exchange(self, identity: str) -> Passthru:
        """
        Identity callback endpoint to exchange an access token
        """
        try:
            path_params = {}
            path_params['identity'] = identity

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/identity/:identity/exchange', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Passthru.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_all(self, app_id: int, app_key: str) -> ConsumerIdentityCollection:
        """
        Returns a paginated list of identities which are relevant to the authenticated user
        """
        try:
            path_params = {}

            query_params = {}
            query_params['appId'] = app_id
            query_params['appKey'] = app_key

            query_struct_names = []

            url = self.parser.url('/consumer/identity', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ConsumerIdentityCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def redirect(self, identity: str) -> Passthru:
        """
        Redirect the user to the configured identity provider
        """
        try:
            path_params = {}
            path_params['identity'] = identity

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/consumer/identity/:identity/redirect', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Passthru.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



