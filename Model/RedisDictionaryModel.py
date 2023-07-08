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
        itemRedistributeIntervalMillisecond:int
        isServerPresentData:bool
class ClientRegisterDataModel:
        clientId:str
        systemId:str
class TopicDataModel:
        topicId:str
        adminClientIds:list[str]
        clientIds:list[str]
        isPrivateTopic:bool
        privateTopicPasscode:str


class SystemBaseDataModel:
        distributeMode:int 
        systemItemId:str
