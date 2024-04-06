"""
ConsumerTransactionTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException

from .common_message_exception import CommonMessageException
from .consumer_transaction import ConsumerTransaction
from .consumer_transaction_collection import ConsumerTransactionCollection

class ConsumerTransactionTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)

    pass


    def get(self, transaction_id: str) -> ConsumerTransaction:
        try:
            path_params = {}
            path_params["transaction_id"] = transaction_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/consumer/transaction/$transaction_id<[0-9]+|^~>", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerTransaction.from_json(response.content)

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

    def get_all(self, start_index: int, count: int, search: str) -> ConsumerTransactionCollection:
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/consumer/transaction", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerTransactionCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    pass


