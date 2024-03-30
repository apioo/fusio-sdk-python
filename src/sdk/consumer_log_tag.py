"""
ConsumerLogTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException

from common_message_exception import CommonMessageException
from consumer_log import ConsumerLog
from consumer_log_collection import ConsumerLogCollection

class ConsumerLogTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)

    pass


    def get(self, log_id: str) -> ConsumerLog:
        try:
            path_params = {}
            path_params["log_id"] = log_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/log/$log_id<[0-9]+>", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerLog.from_json(response.content)

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

    pass

    def get_all(self, start_index: int, count: int, search: str) -> ConsumerLogCollection:
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/consumer/log", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerLogCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass


