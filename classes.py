from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass
class MobileFood(DataClassJsonMixin):
    applicant: str
    status: str
    address: str
    latitude: str
    longitude: str

