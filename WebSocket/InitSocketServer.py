
import asyncio
from websockets.server import serve

from Business.RedisController import   RedisController
from Business.ConfigReader import ConfigReader

class ClientSocket:

    async def echo(websocket):
        async for message in websocket:
            print("Data:"+message)
            await websocket.send(message)

    async def main():
        async with serve(ClientSocket.echo, "0.0.0.0", ConfigReader.GetServerConf("ServerPort")):
            print("Server is running on port "+ConfigReader.GetServerConf("ServerPort"))
            await asyncio.Future()  # run forever

class InitServer:
    def startServerSequence():
        RedisController.ConnectionTest()
        asyncio.run(ClientSocket.main())
