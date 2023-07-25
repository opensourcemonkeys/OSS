from Business.RedisController import RedisController
import socket

class Distributor:
    def SendToMessageWithBackendProxy(node:str,useTCP:bool,data:str):
        if(useTCP):
            print("TCP")




class ClientSocketFilter:
    def SetClientandServerIdtoRedis(clientSystemId:str,serverPort:str):
         hostname=socket.gethostname()
         IPAddr=socket.gethostbyname(hostname)
         node:str = IPAddr +":"+ serverPort
         result = RedisController.UpdateClientNodeId(nodeId=node,clientSystemId=clientSystemId)
    def CheckSystemIdFromSocketPath(clientSystemId: str):
        result = RedisController.GetDataClientRegisterFromSystemId(clientSystemId)
        if not result == None:
            return True
