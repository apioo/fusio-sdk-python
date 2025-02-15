"""
consumer_payment_checkout_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ConsumerPaymentCheckoutRequest(BaseModel):
    plan_id: Optional[int] = Field(default=None, alias="planId")
    return_url: Optional[str] = Field(default=None, alias="returnUrl")
    pass


