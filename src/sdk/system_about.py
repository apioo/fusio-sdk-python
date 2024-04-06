"""
system_about automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from .system_about_apps import SystemAboutApps
from .system_about_link import SystemAboutLink
@dataclass_json
@dataclass
class SystemAbout:
    api_version: str = field(default=None, metadata=config(field_name="apiVersion"))
    title: str = field(default=None, metadata=config(field_name="title"))
    description: str = field(default=None, metadata=config(field_name="description"))
    terms_of_service: str = field(default=None, metadata=config(field_name="termsOfService"))
    contact_name: str = field(default=None, metadata=config(field_name="contactName"))
    contact_url: str = field(default=None, metadata=config(field_name="contactUrl"))
    contact_email: str = field(default=None, metadata=config(field_name="contactEmail"))
    license_name: str = field(default=None, metadata=config(field_name="licenseName"))
    license_url: str = field(default=None, metadata=config(field_name="licenseUrl"))
    payment_currency: str = field(default=None, metadata=config(field_name="paymentCurrency"))
    categories: List[str] = field(default=None, metadata=config(field_name="categories"))
    scopes: List[str] = field(default=None, metadata=config(field_name="scopes"))
    apps: SystemAboutApps = field(default=None, metadata=config(field_name="apps"))
    links: List[SystemAboutLink] = field(default=None, metadata=config(field_name="links"))
