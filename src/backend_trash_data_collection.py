"""
backend_trash_data_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_collection import CommonCollection
from backend_trash_data import BackendTrashData
@dataclass_json
@dataclass
class BackendTrashDataCollection(CommonCollection[BackendTrashData]):
    pass
