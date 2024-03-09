"""
BackendTransactionTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from backend_transaction import BackendTransaction
from backend_transaction_collection import BackendTransactionCollection
from common_message_exception import CommonMessageException

class BackendTransactionTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def get(self, transaction_id: str) -> BackendTransaction:
        try:
            pathParams = {}
            pathParams["transaction_id"] = transaction_id

            queryParams = {}

            queryStructNames = [];

            url = self.parser.url("/backend/transaction/$transaction_id<[0-9]+>", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendTransaction.from_json(response.content)

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

    def get_all(self, start_index: int, count: int, search: str, _from: str, to: str, plan_id: int, user_id: int, app_id: int, status: str, provider: str) -> BackendTransactionCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search
            queryParams["from"] = _from
            queryParams["to"] = to
            queryParams["planId"] = plan_id
            queryParams["userId"] = user_id
            queryParams["appId"] = app_id
            queryParams["status"] = status
            queryParams["provider"] = provider

            queryStructNames = [];

            url = self.parser.url("/backend/transaction", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendTransactionCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


