
import asyncio
import uvicorn
from Server.Base import app

from Business.RedisController import   RedisController
from Business.ConfigReader import ConfigReader

class InitServer:
    def startServerSequence():
        RedisController.ConnectionTest()
        uvicorn.run(app=app,port=10500)
