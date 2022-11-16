import asyncio

from loguru import logger


class Synchroniser:
    def __init__(self):
        self.d: dict[str, asyncio.Event] = {}

    def create(self, event: str):
        self.d[event] = asyncio.Event()

    async def wait(self, event: str):
        if event not in self.d.keys():
            self.create(event=event)

        await self.d[event].wait()

    def set(self, event: str):
        if event not in self.d.keys():
            self.create(event=event)

        self.d[event].set()
        logger.info(f"{event}: set")


synchroniser = Synchroniser()
