# -*- coding: utf-8 -*-
from redisservice import cache
import random
import time

@cache
def foo(n):
    return n * 2


# print foo(10)  # first call with parameter 10, sleeps
# print foo(10)  # returns immediately
# print foo(15)  # returns immediately
# print foo(19)  # returns immediately
# print foo(10)  # returns immediately
# print foo(10)  # returns immediately
# print foo(15)  # returns immediately


# symbol = 'eth'
# _len = len(symbol)
# print _len
# _i_usdt = _len - symbol.rfind('usdt') - 4
# _i_eth = _len - symbol.rfind('eth') - 3
# _i_btc = _len - symbol.rfind('btc') - 3
# print _i_usdt
# print _i_eth
# print _i_btc

# symbol = 'EOSBTC/BA/PRICE'
# symbol2 = 'EOSBTC/BA/PRICE 中文'
#
# def judge_pure_english(keyword):
#     return all(ord(c) < 128 for c in keyword)
#
# print(judge_pure_english(symbol))
# print(judge_pure_english(symbol2))

print(random.randint(1, 30) / 10.0)
print(random.randint(1, 30) / 10.0)
print(random.randint(1, 30) / 10.0)
print(random.randint(1, 30) / 10.0)
print(random.randint(1, 30) / 10.0)

time.sleep(2.2)