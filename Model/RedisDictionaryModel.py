from decimal import Decimal

class TreeAxisObjectCoordinates:
        x:Decimal
        y:Decimal
        z:Decimal
class ClientBaseDataModel:
        topicId:str
        clientId:str
        data:str
        treeAxisObjectCoordinates:TreeAxisObjectCoordinates
        isServerPresentData:bool
class SystemDistributeMode:
        replicated:int=1
        shared:int=2
        bothof:int=3
class SystemBaseDataModel:
        distributedNode:SystemDistributeMode
        distributeMode:int 
        systemItemId:str


        