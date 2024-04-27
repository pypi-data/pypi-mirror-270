import asyncio
import json
import logging

from okx.utils import run_async_task
from okx.websocket import WsUtils
from okx.websocket.WebSocketFactory import WebSocketFactory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WsPrivate")


class WsPrivateAsync:
    def __init__(self, apiKey, passphrase, secretKey, url, useServerTime):
        self.url = url
        self.subscriptions = set()
        self.callback = None
        self.factory = WebSocketFactory(url)
        self.apiKey = apiKey
        self.passphrase = passphrase
        self.secretKey = secretKey
        self.useServerTime = useServerTime

    async def connect(self):
        self.websocket = await self.factory.connect()

    async def consume(self):
        async for message in self.websocket:
            if self.callback:
                self.callback(message)

    async def subscribe(self, params: list, callback):
        self.callback = callback

        logRes = await self.login()
        await asyncio.sleep(5)
        if logRes:
            payload = json.dumps({"op": "subscribe", "args": params})
            await self.websocket.send(payload)
        # await self.consume()

    async def login(self):
        loginPayload = await WsUtils.initLoginParams(
            useServerTime=self.useServerTime,
            apiKey=self.apiKey,
            passphrase=self.passphrase,
            secretKey=self.secretKey,
        )
        await self.websocket.send(loginPayload)
        return True

    async def unsubscribe(self, params: list, callback):
        self.callback = callback
        payload = json.dumps({"op": "unsubscribe", "args": params})
        logger.info(f"unsubscribe: {payload}")
        await self.websocket.send(payload)

    async def stop(self):
        await self.factory.close()

    async def start(self):
        logger.info("Connecting to WebSocket...")
        await self.connect()
        run_async_task(self.consume())

    def stop_sync(self):
        asyncio.get_running_loop().run_until_complete(self.stop())
