"""
common_form_element_select_option automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
@dataclass_json
@dataclass
class CommonFormElementSelectOption:
    key: str = field(default=None, metadata=config(field_name="key"))
    value: str = field(default=None, metadata=config(field_name="value"))
