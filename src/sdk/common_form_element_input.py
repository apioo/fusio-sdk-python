"""
common_form_element_input automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from common_form_element import CommonFormElement
@dataclass_json
@dataclass
class CommonFormElementInput(CommonFormElement):
    type: str = field(default=None, metadata=config(field_name="type"))
