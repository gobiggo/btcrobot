# -*- coding: utf-8 -*-

from wxpy import *
import time
import random
from robot_coin import auto_query_coin_price

TULING_KEY = '12f1fc86573e49498efe7882746aa66d'

# 初始化微信机器人
bot = Bot(cache_path=True, console_qr=True)

# 初始化tuling 机器人
# tuling = Tuling(api_key=TULING_KEY)

# 进行测试的好友
my_friend = ensure_one(bot.search('龙光'))
print(my_friend)

# 进行测试的
# my_group = bot.groups().search('wxpy 交流群')[0]
# print(my_group)

@bot.register(my_friend, TEXT)
def auto_reply_coin_price(msg):
    # 增加延迟
    time.sleep(random.randint(1, 30) / 10.0)
    return auto_query_coin_price(msg.text)

# @bot.register(Friend, TEXT)
def auto_reply_all_friend(msg):
    # 增加延迟
    time.sleep(random.randint(1, 30) / 10.0)
    return auto_query_coin_price(msg.text)

# 堵塞线程，并进入 Python 命令行
# embed()
# 阻塞进程
bot.join()
