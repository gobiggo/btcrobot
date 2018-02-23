# -*- coding: utf-8 -*-

import sys
from binance import Binance
from huobi import HuoBi
from okex import OKEX
from zb import ZB
from coinmarketcap import CoinMarketCap
from logger import Logger
from config import EXCHANGES
import re
import time
import random

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

from wxpy import *

# reload(sys)
# sys.setdefaultencoding("utf-8")

TULING_KEY = '12f1fc86573e49498efe7882746aa66d'

# 初始化微信机器人
bot = Bot(cache_path=True, console_qr=True)

# 初始化tuling 机器人
# tuling = Tuling(api_key=TULING_KEY)

# 进行测试的好友
my_friend = ensure_one(bot.search('龙光'))
print(my_friend)

ba = Binance()
okex = OKEX()
huobi = HuoBi()
zb = ZB()
coincap = CoinMarketCap()
logger = Logger().get_log()


def query_price_by_exchange(_exchange, _symbol):
    if _symbol and _exchange and len(_symbol) > 2 and len(_exchange) > 1:
        if 'HB' == _exchange:
            return huobi.get_coin_price_api(_symbol)
        elif 'BA' == _exchange:
            return ba.get_coin_price_api(_symbol)
        elif 'OK' == _exchange:
            return okex.get_coin_price_api(_symbol)
        elif 'ZB' == _exchange:
            return zb.get_coin_price_api(_symbol)
        elif 'CMC' == _exchange:
            return coincap.get_coin_price_api(_symbol)
        else:
            return coincap.get_coin_price_api(_symbol)

    return None


@bot.register(my_friend, TEXT)
def auto_reply_coin_price(msg):
    # 增加延迟
    time.sleep(random.randint(1, 30) / 10.0)
    return auto_query_coin_price(msg.text)


def judge_pure_english(keyword):
    try:
        return all(ord(c) < 128 for c in keyword)
    except Exception:
        return False


# def contain_zh(word):
#     """
#     判断传入字符串是否包含中文
#     :param word: 待判断字符串
#     :return: True:包含中文  False:不包含中文
#     """
#     word = word.decode()
#     global zh_pattern
#     match = zh_pattern.search(word)
#
#     return match

def auto_query_coin_price(msg):
    """
    自动报价
    # msg 格式要求: <交易对>/<交易所>/<功能>/<功能参数>;EOSBTC/BA/PRICE
    # <交易对> 格式为 <基础货币>_<报价货币>，例如eth_usdt: 返回的是eth的usdt价格。报价货币不填则默认为usdt
    # <交易所> 格式为['HB', 'BA', 'OK', 'ZB','CMC']其中一个交易所，分别代表火币、币安、OKEX、中币和CoinMarketCap；交易所不填默认为BA
    # <功能> 格式为['PRICE','KLINE','DEPTH']，分别代表查询价格、k线和深度。只有'HB' 和'BA'交易所支持<功能>模块；<功能>可以省略，默认为'price'，有<功能>则必须带<交易所>
    # <功能参数> DEPTH[Limit] KLINE[itv={1m,1h,2h,4h,12h,1d,1w,1M}]
    # DEPTH limit=10/50/100, 并不返回全部详细数据，而是反馈所有挂单的总和，入limit=50 则返回 前50个买单和卖单 的数量总和
    :param msg: 查询的交易对
    :return: 
    """
    if not judge_pure_english(msg):
        return
    if msg == '--help':
        return '<交易对>/<交易所>/<功能>/<功能参数>\n交易对:<基础货币>_<报价货币>\n交易所:HB,BA,OK,ZB,CMC\n功能:PRICE/DEPTH\n功能参数:limit=10/50/100'

    logger.info(msg)
    _strs = msg.split('/')
    _len = len(_strs)
    if _len == 1:
        # 直接查询价格
        return ba.get_coin_price_api(_strs[0])
    if _len == 2 or (_len >= 3 and _strs[2] == 'PRICE'):
        _symbol = _strs[0]
        _exchange = _strs[1]
        return query_price_by_exchange(_exchange, _symbol)
    if _len >= 3 and _strs[2] == 'DEPTH':
        return '敬请期待'

def test():
    print(auto_query_coin_price('EOS_BC/BA/PRICE'))
    print(auto_query_coin_price('EOSBTC/'))
    print(auto_query_coin_price('eOS_BTC/ZB/PRICE'))
    print(auto_query_coin_price('/EOSBTC/OK/PRICE'))
    print(auto_query_coin_price('BTC/CMC/PRICE'))
    print(auto_query_coin_price('NAS'))
    print(auto_query_coin_price('--help'))
    print(auto_query_coin_price('NASETH/HB'))
    print(auto_query_coin_price('NASETH/HB/DEPTH'))
    print(auto_query_coin_price('中文试试'))


# test()


# 堵塞线程，并进入 Python 命令行
# embed()
# 阻塞进程
bot.join()