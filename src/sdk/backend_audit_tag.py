"""
BackendAuditTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .backend_audit import BackendAudit
from .backend_audit_collection import BackendAuditCollection
from .common_message_exception import CommonMessageException

class BackendAuditTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get(self, audit_id: str) -> BackendAudit:
        try:
            path_params = {}
            path_params['audit_id'] = audit_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/audit/$audit_id<[0-9]+>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendAudit.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_all(self, start_index: int, count: int, search: str, from_: str, to: str, app_id: int, user_id: int, event: str, ip: str, message: str) -> BackendAuditCollection:
        try:
            path_params = {}

            query_params = {}
            query_params['startIndex'] = start_index
            query_params['count'] = count
            query_params['search'] = search
            query_params['from'] = from_
            query_params['to'] = to
            query_params['appId'] = app_id
            query_params['userId'] = user_id
            query_params['event'] = event
            query_params['ip'] = ip
            query_params['message'] = message

            query_struct_names = []

            url = self.parser.url('/backend/audit', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendAuditCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



