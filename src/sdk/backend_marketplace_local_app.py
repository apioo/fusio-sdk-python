"""
backend_marketplace_local_app automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from backend_marketplace_app import BackendMarketplaceApp
@dataclass_json
@dataclass
class BackendMarketplaceLocalApp(BackendMarketplaceApp):
    remote: BackendMarketplaceApp
