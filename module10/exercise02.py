import asyncio
import json

import websockets


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame);
        print(trade)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


asyncio.run(connect())
