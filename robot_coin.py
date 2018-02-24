# -*- coding: utf-8 -*-

from api_binance import Binance
from api_huobi import HuoBi
from api_okex import OKEX
from api_zb import ZB
from api_coinmarketcap import CoinMarketCap
from config import EXCHANGES
from config import FUNCTIONS
import re

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

ba = Binance()
okex = OKEX()
huobi = HuoBi()
zb = ZB()
coincap = CoinMarketCap()


def judge_pure_english(keyword):
    try:
        return all(ord(c) < 128 for c in keyword)
    except Exception:
        return False


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


def auto_query_coin_price(msg):
    """
    自动报价
    # msg 格式要求: 
    # :<交易对>/<交易所> 或者 <交易对>/<功能>/<功能参数>;:EOSBTC/BA 或者 :ETH_USDT/DEPTH/limit=10
    # 以`:` 开头，表示对话机器人；以`/`作为参数之间的分隔符；所有字符均为英文字符，机器人只会回复格式匹配的对话
    # <交易对> 格式为 <基础货币>_<报价货币>，例如eth_usdt: 返回的是eth的usdt价格。报价货币不填则默认为usdt
    # <交易所> 格式为['HB', 'BA', 'OK', 'ZB','CMC']其中一个交易所，分别代表火币、币安、OKEX、中币和CoinMarketCap；交易所不填默认为BA
    # <功能> 格式为['KLINE','DEPTH']，分别代表k线和深度，功能模块均为BA(币安)的数据。
    # <功能参数> DEPTH[Limit] KLINE[itv={1m,1h,2h,4h,12h,1d,1w,1M}]
    # DEPTH limit=10/50/100, 并不返回全部详细数据，而是反馈所有挂单的总和，入limit=50 则返回 前50个买单和卖单 的数量总和
    :param msg: 查询的交易对等参数
    :return: 
    """
    if not judge_pure_english(msg):
        return
    if msg.index(':') != 0:
        return
    if msg == ':help':
        return ':<交易对>/<交易所> 或者 :<交易对>/<功能>/<功能参数>\n交易对:<基础货币>_<报价货币>\n交易所:HB,BA,OK,ZB,CMC' \
               '\n功能:KLINE/DEPTH\n功能参数:limit=10/50/100'

    _strs = msg.replace(':', '').split('/')
    _len = len(_strs)
    if _len == 1:
        # 直接查询价格
        return ba.get_coin_price_api(_strs[0])
    if _len == 2 and (_strs[1] in EXCHANGES):
        _symbol = _strs[0]
        _exchange = _strs[1]
        return query_price_by_exchange(_exchange, _symbol)
    if _len >= 2 and (_strs[1] in FUNCTIONS):
        _symbol = _strs[0]
        _function = _strs[1]
        return "敬请期待"


def test():
    print(auto_query_coin_price(':EOS_BC/BA'))
    print(auto_query_coin_price(':EOSBTC/'))
    print(auto_query_coin_price('eOS_BTC/ZB'))
    print(auto_query_coin_price(':/EOSBTC/OK'))
    print(auto_query_coin_price(':BTC/CMC'))
    print(auto_query_coin_price(':NAS'))
    print(auto_query_coin_price(':help'))
    print(auto_query_coin_price(':NASETH/HB'))
    print(auto_query_coin_price(':NASETH/HB/DEPTH'))
    print(auto_query_coin_price(':中文试试'))

test()
