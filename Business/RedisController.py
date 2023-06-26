import redis
import asyncio
import uuid
from datetime import datetime


class RedisController:
    async def setItemTest(itemSet, keyno):
        itemSet.set('OSS_'+str(keyno),
                    'OSS redis connection test.  '+str(keyno))
        print(keyno)

    def ConnectionTest():
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rediss = redis.Redis(connection_pool=pool)
        rediss.flushdb
        rediss.config_set("save", "")
        now = datetime.now()
        print("START date and time:", now)
        asyncio.run(RedisController.setItemTest(rediss, str(uuid.uuid4())))
        now = datetime.now()
        print("STOP date and time:", now)
        value = rediss.get('OSS')
        print(value)

    def setData(topicID, DATA):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rd.set(topicID, DATA)

    def dropData(topicID):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        rd.delete(topicID)

    def getData(topicID:str=None,containsTextIn:str=None,enableContainFilter:bool=False):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rd = redis.Redis(connection_pool=pool)
        
        rs=rd.ft("dataIndex")
        ### todo not tested
        if enableContainFilter:
            result=rs.search( query=containsTextIn).docs
            return result
        

    