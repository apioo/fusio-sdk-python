"""
consumer_event automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from common_metadata import CommonMetadata
@dataclass_json
@dataclass
class ConsumerEvent:
    id: int
    name: str
    description: str
    metadata: CommonMetadata
