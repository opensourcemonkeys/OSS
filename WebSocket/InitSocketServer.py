
import asyncio
from websockets.server import serve

from Business.RedisController import   RedisController

class ClientSocket:

    async def echo(websocket):
        async for message in websocket:
            print("Data:"+message)
            await websocket.send(message)

    async def main():
        async with serve(ClientSocket.echo, "0.0.0.0", 10100):
            await asyncio.Future()  # run forever

class initServer:
    def startServerSequence():
        RedisController.ConnectionTest()
        asyncio.run(ClientSocket.main())
