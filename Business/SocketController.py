from Business.RedisController import RedisController


class ClientDistributor:

    def SentToTopicsByQueryResult():
        print("")


class ServerDistributor:
    def Set():
        print("")

    def Get():
        print("")

    def Delete():
        print("")

    def Update():
        print("")


class ClientSocketFilter:
    def CheckSystemIdFromSocketPath(clientSystemId: str):
        result = RedisController.GetDataClientRegisterFromSystemId(
            clientSystemId)
        if not result == None:

            return True
