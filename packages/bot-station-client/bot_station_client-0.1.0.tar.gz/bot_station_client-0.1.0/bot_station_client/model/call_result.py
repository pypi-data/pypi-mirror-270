import json
import logging

from bot_station_client.model.document import Document


class CallResult:
    text: str
    relevant_docs: list[Document]

    def __init__(self, json_string):
        self.__dict__ = json.loads(json_string)
