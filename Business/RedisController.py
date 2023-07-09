import json
import redis
import asyncio
import uuid
from datetime import datetime
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query
from Model.RedisDictionaryModel import ClientBaseDataModel, TreeAxisObjectCoordinates


class RedisConnectionOperators:
    def ConnectionPool():
        pool = redis.ConnectionPool(host='redis-stack-server', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        return rd

    def CreateRedisJsonIndex(fields=[TextField], indexItemKeyPrefix=str):
        pool = redis.ConnectionPool(host='redis-stack-server', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rs = rd.ft("idx:"+indexItemKeyPrefix)
        schema = (fields
                  )
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=[indexItemKeyPrefix], index_type=IndexType.JSON
            )
        )


class RedisController:

    systemItemPrefix = "OSS"
    systemClientRegisterPrefix = "ClientRegister"

    async def setItemTest(data):
        result = RedisController.setData(data)
        print(result)

    def ConnectionTest():
        dictItem = ClientBaseDataModel()
        dictItem.topicId = str(uuid.uuid4())
        dictItem.data = "This is redis data test message"
        dictItem.isServerPresentData = True
        dictItem.clientId = "sampleClient"
        itemCoordinates = TreeAxisObjectCoordinates()
        itemCoordinates.x = 1.5468
        itemCoordinates.y = 1.1542
        itemCoordinates.z = 1.2348
        dictItem.treeAxisObjectCoordinates = itemCoordinates

        dictItem.treeAxisObjectCoordinates = itemCoordinates.__dict__


        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rediss = redis.Redis(connection_pool=pool)
        rediss.flushdb()
        rediss.flushall()
        rediss.config_set("save", "")
        now = datetime.now()
        print("START date and time:", now)
        indexFields = (TextField("$.clientId", as_name="clientId"),
                       TextField("$.systemId", as_name="systemId"))
        RedisConnectionOperators.CreateRedisJsonIndex(indexFields,RedisController.systemItemPrefix)
        asyncio.run(RedisController.setItemTest(dictItem.__dict__))
        now = datetime.now()
        print("STOP date and time:", now)
        valueQueryResult = RedisController.getData(
            query="sampleClient")
        if len(valueQueryResult) > 0:
            print("Query Test Result:"+valueQueryResult[0]["id"])

    def setData(data: str):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        itemId = RedisController.systemItemPrefix + str(uuid.uuid4())
        rd.json().set(itemId, Path.root_path(), data)
        rd.close()
        return True

    def dropData(topicID: str):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rd.delete(topicID)

    def getData(query: str = None):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rs = rd.ft("idx:"+RedisController.systemItemPrefix)
        result = rs.search(Query(query)).docs
        return result

    def setDataClientRegister(clientId: str):
        keyprefix = RedisController.systemItemPrefix + \
            RedisController.systemClientRegisterPrefix
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        itemId = keyprefix + str(uuid.uuid4())
        systemId = str(uuid.uuid4()).replace("-", "")
        rs = rd.ft("idx:"+keyprefix)
        schema = (
            TextField("$.clientId", as_name="clientId"),
            TextField("$.systemId", as_name="systemId"),
        )
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=[keyprefix], index_type=IndexType.JSON
            )
        )
        data = {
            "clientId": clientId,
            "systemId": systemId,
            "registerDate": str(datetime.now())
        }
        rd.json().set(itemId, Path.root_path(), data)
        rd.close()
        return systemId

    def GetDataClientRegisterFromSystemId(systemId: str = None, enableContainFilter: bool = True):
        keyprefix = RedisController.systemItemPrefix + \
            RedisController.systemClientRegisterPrefix
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rs = rd.ft("idx:"+keyprefix)
        if enableContainFilter:

            result = rs.search(Query(systemId),

                               ).docs
            return result

    def DropDataClientRegister(clientId: str, topicId: str):
        keyprefix = RedisController.systemItemPrefix + \
            RedisController.systemClientRegisterPrefix
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        itemId = keyprefix + str(uuid.uuid4())
        rs = rd.ft("idx:"+keyprefix)
        schema = (
            TextField("$.topicId", as_name="topicId"),
            TextField("$.clientId", as_name="clientId"),
        )
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=[keyprefix], index_type=IndexType.JSON
            )
        )
        data = {
            "topicId": topicId,
            "clientId": clientId,

        }
        rd.json().set(itemId, Path.root_path(), data)
        rd.close()
        return itemId
