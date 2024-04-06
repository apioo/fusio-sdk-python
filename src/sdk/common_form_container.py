"""
common_form_container automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from typing import Union
from .common_form_element_input import CommonFormElementInput
from .common_form_element_select import CommonFormElementSelect
from .common_form_element_tag import CommonFormElementTag
from .common_form_element_text_area import CommonFormElementTextArea
@dataclass_json
@dataclass
class CommonFormContainer:
    element: List[Union[CommonFormElementInput, CommonFormElementSelect, CommonFormElementTag, CommonFormElementTextArea]] = field(default=None, metadata=config(field_name="element"))
