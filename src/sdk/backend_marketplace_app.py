"""
backend_marketplace_app automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
@dataclass_json
@dataclass
class BackendMarketplaceApp:
    version: str = field(metadata=config(field_name="version"))
    description: str = field(metadata=config(field_name="description"))
    screenshot: str = field(metadata=config(field_name="screenshot"))
    website: str = field(metadata=config(field_name="website"))
    download_url: str = field(metadata=config(field_name="downloadUrl"))
    sha_hash: str = field(metadata=config(field_name="sha1Hash"))
    start_url: str = field(metadata=config(field_name="startUrl"))
