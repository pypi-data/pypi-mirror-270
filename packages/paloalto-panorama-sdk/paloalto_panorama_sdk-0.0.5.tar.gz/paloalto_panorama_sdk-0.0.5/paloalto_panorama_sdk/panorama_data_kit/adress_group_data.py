from dataclasses import dataclass
from typing import List, Dict

@dataclass
class AddressGroup:
    location: str
    name: str
    description: str
    static: 'StaticMembers'

    @dataclass
    class StaticMembers:
        member: List[str]

    @classmethod
    def from_json(cls, json_data: Dict):
        location = json_data.get('@location')
        name = json_data.get('@name')
        description = json_data.get('description')
        static = json_data.get('static', {}).get('member')
        return cls(location, name, description, static)
