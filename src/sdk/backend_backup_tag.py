"""
BackendBackupTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .backend_backup_export import BackendBackupExport
from .backend_backup_import import BackendBackupImport
from .backend_backup_import_result import BackendBackupImportResult
from .common_message_exception import CommonMessageException

class BackendBackupTag(sdkgen.TagAbstract):
    @classmethod
    def __init__(cls, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    @classmethod
    def import_(cls, payload: BackendBackupImport) -> BackendBackupImportResult:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/backend/backup/import", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = cls.http_client.post(url, headers=headers, params=cls.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendBackupImportResult.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    @classmethod
    def export(cls) -> BackendBackupExport:
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = cls.parser.url("/backend/backup/export", path_params)

            headers = {}

            response = cls.http_client.post(url, headers=headers, params=cls.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BackendBackupExport.model_validate_json(json_data=response.content)

            if response.status_code == 401:
                raise CommonMessageException(response.content)
            if response.status_code == 500:
                raise CommonMessageException(response.content)

            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


