# -*- coding: utf-8 -*-
from service_redis_cache import *
from robot_coin import auto_query_coin_price
import time

db = RedisCache('test_cache')


# @redis_cached(db, 10)
def query(msg):
    print(auto_query_coin_price(msg))


t = time.time()
query(':ETH')
print(time.time() - t)

t = time.time()
query(':ETH')
print(time.time() - t)

time.sleep(11)

t = time.time()
query(':ETH')
print(time.time() - t)

t = time.time()
query(':ETH')
print(time.time() - t)
