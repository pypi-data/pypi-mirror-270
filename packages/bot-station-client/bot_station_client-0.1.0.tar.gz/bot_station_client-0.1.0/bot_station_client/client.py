import json
import logging
import uuid
from typing import Dict

import aiohttp

from bot_station_client.model.call_result import CallResult
from bot_station_client.model.config import BotStationClientConfig


class BotStationClient:
    config: BotStationClientConfig = ""

    def __init__(self, config: BotStationClientConfig):
        self.config = config

    async def create(self,
                     name: str,
                     description: str,
                     prompt_intro: str,
                     add_external_context_to_prompt: bool = False,
                     add_messages_history_to_prompt: bool = False,
                     temperature: float = 0.6
                     ) -> str:
        """
        :param name:
        :param description:
        :param prompt_intro:
        :param add_external_context_to_prompt:
        :param add_messages_history_to_prompt:
        :param temperature:
        :return: new bot's ID
        """
        response_json = await self.__post(
            method="create",
            content={
                "name": name,
                "description": description,
                "prompt_intro": prompt_intro,
                "add_external_context_to_prompt": str(add_external_context_to_prompt).lower(),
                "add_messages_history_to_prompt": str(add_messages_history_to_prompt).lower(),
                "temperature": temperature,
            }
        )
        return str(response_json["id"])

    async def train(self,
                    bot_id: str,
                    text: str,
                    id: str = str(uuid.uuid4()),
                    source_link: str | None = None,
                    metadata: dict[str, str] | None = None,
                    ):
        content = {"bot_id": bot_id, "data": text, "id": id}

        if source_link is not None:
            content["source_link"] = source_link
        if metadata is not None:
            content["metadata"] = metadata

        await self.__post(
            method="train",
            content=content
        )

    async def call(self,
                   bot_id: str,
                   chat_id: int | str,
                   text: str
                   ) -> CallResult:
        """
        :param bot_id:
        :param chat_id:
        :param text:
        :return: bot's response
        """
        response_dict = await self.__post(
            method="call",
            content={
                "bot_id": bot_id,
                "chat_id": chat_id,
                "data": text
            }
        )
        response_str = json.dumps(response_dict)
        result = CallResult(response_str)

        return result

    async def __post(self,
                     method: str,
                     content: Dict[str, str | int],
                     ) -> dict[str, object]:
        """
        Returns response json body
        """
        headers: Dict[str, str] = {'content-type': 'application/json'}
        session = aiohttp.ClientSession(headers=headers)
        url = f'{self.config.base_uri}/{method}'
        logging.debug(f"POST /{method}  {content}")
        response = await session.post(url=url, data=json.dumps(content))
        if response.status == 200:
            if response.content_type == 'application/json':
                data = await response.json()
            else:
                data = {}
            await session.close()
            return data
        else:
            await session.close()
            raise Exception(f"{response.status} {response.content}")
