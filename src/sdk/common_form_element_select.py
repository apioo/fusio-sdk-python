"""
common_form_element_select automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from common_form_element import CommonFormElement
from common_form_element_select_option import CommonFormElementSelectOption
@dataclass_json
@dataclass
class CommonFormElementSelect(CommonFormElement):
    options: List[CommonFormElementSelectOption] = field(default=None, metadata=config(field_name="options"))
