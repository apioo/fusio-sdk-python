"""
BackendLogTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .backend_log import BackendLog
from .backend_log_collection import BackendLogCollection
from .backend_log_error import BackendLogError
from .backend_log_error_collection import BackendLogErrorCollection
from .common_message import CommonMessage
from .common_message_exception import CommonMessageException

class BackendLogTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get(self, log_id: str) -> BackendLog:
        """
        Returns a specific log
        """
        try:
            path_params = {}
            path_params['log_id'] = log_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/log/$log_id<[0-9]+>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendLog.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_all(self, start_index: int, count: int, search: str, from_: str, to: str, operation_id: int, app_id: int, user_id: int, ip: str, user_agent: str, method: str, path: str, header: str, body: str) -> BackendLogCollection:
        """
        Returns a paginated list of logs
        """
        try:
            path_params = {}

            query_params = {}
            query_params['startIndex'] = start_index
            query_params['count'] = count
            query_params['search'] = search
            query_params['from'] = from_
            query_params['to'] = to
            query_params['operationId'] = operation_id
            query_params['appId'] = app_id
            query_params['userId'] = user_id
            query_params['ip'] = ip
            query_params['userAgent'] = user_agent
            query_params['method'] = method
            query_params['path'] = path
            query_params['header'] = header
            query_params['body'] = body

            query_struct_names = []

            url = self.parser.url('/backend/log', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendLogCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_all_errors(self, start_index: int, count: int, search: str) -> BackendLogErrorCollection:
        """
        Returns a paginated list of log errors
        """
        try:
            path_params = {}

            query_params = {}
            query_params['startIndex'] = start_index
            query_params['count'] = count
            query_params['search'] = search

            query_struct_names = []

            url = self.parser.url('/backend/log/error', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendLogErrorCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_error(self, error_id: str) -> BackendLogError:
        """
        Returns a specific error
        """
        try:
            path_params = {}
            path_params['error_id'] = error_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/backend/log/error/$error_id<[0-9]+>', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = BackendLogError.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = CommonMessage.model_validate_json(json_data=response.content)

                raise CommonMessageException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



