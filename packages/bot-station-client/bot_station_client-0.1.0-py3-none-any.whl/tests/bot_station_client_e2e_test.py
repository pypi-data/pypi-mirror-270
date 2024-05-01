import logging
import unittest

import aiohttp

from bot_station_client.client import BotStationClient
from bot_station_client.model.config import BotStationClientConfig

logging.basicConfig(format='%(asctime)s.%(msecs)06f %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG)

base_uri = "http://0.0.0.0:8000"

config = BotStationClientConfig(base_uri=base_uri)
bot_station_client: BotStationClient = BotStationClient(config)


class BotStationApiTest(unittest.IsolatedAsyncioTestCase):

    async def test_train(self):
        bot_id = await self.__test_create()
        await bot_station_client.train(
            bot_id=bot_id,
            text="FastAPI is a modern, fast, web framework for building APIs with Python.",
            source_link="http://test.py",
        )
        self.assertTrue(True)
        await self.__test_admin_delete(bot_id)

    async def test_call(self):
        bot_id = await self.__test_create()
        response = await bot_station_client.call(
            bot_id=bot_id,
            chat_id=1,
            text="What is FastAPI?"
        )
        logging.debug(f"Response = {response.text}")
        self.assertIsNotNone(response)
        await self.__test_admin_delete(bot_id)

    @staticmethod
    async def __test_create() -> str:
        bot_id = await bot_station_client.create(
            name="name",
            description="description",
            prompt_intro="You are programmer's assistant",
            temperature=0.6
        )
        logging.debug(f"Response bot_id = {bot_id}")
        return bot_id

    @staticmethod
    async def __test_admin_delete(bot_id: str):
        logging.debug("Tear down. Remove bot")
        session = aiohttp.ClientSession()
        await session.delete(url=f"{base_uri}/admin/{bot_id}")
        await session.close()


if __name__ == '__main__':
    unittest.main()
