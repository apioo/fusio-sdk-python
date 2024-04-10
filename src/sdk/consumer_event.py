"""
consumer_event automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from .common_metadata import CommonMetadata
@dataclass_json
@dataclass
class ConsumerEvent:
    id: int = field(default=None, metadata=config(field_name="id"))
    name: str = field(default=None, metadata=config(field_name="name"))
    description: str = field(default=None, metadata=config(field_name="description"))
    metadata: CommonMetadata = field(default=None, metadata=config(field_name="metadata"))
