from asyncio import sleep
from fastapi import FastAPI, WebSocket
from Business.RedisController import RedisController
from Business.SocketController import ClientSocketFilter
app = FastAPI()


@app.get("/")
async def root():

    return {"message": "This is OSS"}


@app.post("/user/register")
async def SetUser(clientId: str):
    UserSystemId = RedisController.setDataClientRegister(clientId)
    return {"UserSystemId": UserSystemId}
# User activity will trace and delete with spesific conditions


@app.post("/topic/create")
async def SetTopic():
    return {"message": "This is OSS"}


@app.delete("/topic/delete")
async def DeleteTopic():
    return {"message": "This is OSS"}


# ws://servername:port/ws-client
@app.websocket("/ws-streamtest")
async def ClientSocketStreamTest(websocket: WebSocket):
    await websocket.accept()
    while True:
            data = RedisController.getData("sampleClient")
            await sleep(0.001 )
            await websocket.send_text(f""+str(data[0]))


@app.websocket("/ws-client/{registerToken}")
async def ClientSocket(websocket: WebSocket, registerToken: str):
    if not (registerToken == "" or registerToken == None):
        socketAvailability = ClientSocketFilter.CheckSystemIdFromSocketPath(
            registerToken)
        if (socketAvailability):
            socketPort= websocket.scope.get("server")
            ClientSocketFilter.SetClientandServerIdtoRedis(registerToken,str(socketPort[1]))
            await websocket.accept()
    while True:
        data = await websocket.receive_text()
        
        await websocket.send_text(f"Message text was: {data}")


@app.websocket("/ws-server")
async def ServerSocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
