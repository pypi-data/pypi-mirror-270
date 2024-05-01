import json
from dataclasses import dataclass


@dataclass
class Document:
    id: str
    data: str
    source_link: str | None
    metadata: dict | None

    def __init__(self, json_string):
        self.__dict__ = json.loads(json_string)
