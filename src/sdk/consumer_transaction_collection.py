"""
consumer_transaction_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from common_collection import CommonCollection
from consumer_transaction import ConsumerTransaction
@dataclass_json
@dataclass
class ConsumerTransactionCollection(CommonCollection[ConsumerTransaction]):
    pass
