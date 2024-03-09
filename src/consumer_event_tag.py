"""
ConsumerEventTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from common_message_exception import CommonMessageException
from consumer_event_collection import ConsumerEventCollection

class ConsumerEventTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    def get_all(self, start_index: int, count: int, search: str) -> ConsumerEventCollection:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            queryStructNames = [];

            url = self.parser.url("/consumer/event", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=this.parser.query(queryParams, queryStructNames))

            if response.status_code >= 200 and response.status_code < 300:
                return ConsumerEventCollection.from_json(response.content)

            if response.status_code == 401:
                raise CommonMessageException(CommonMessage.from_json(response.content))
            if response.status_code == 500:
                raise CommonMessageException(CommonMessage.from_json(response.content))

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


