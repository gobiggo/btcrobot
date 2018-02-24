# -*- coding: utf-8 -*-
# @Date    : 2017-12-15 15:40:03
# @Author  : KlausQiu
# @QQ      : 375235513
# @github  : https://github.com/KlausQIU

# from huobi_util import *
from util_tools import http_get_request
from config import HB_MARKET_URL as MARKET_URL

'''
Market data API
'''


# 获取KLine


def get_kline(symbol, period, size):
    """
    :param symbol
    :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
    :param size: [1,2000]
    :return:
    """
    params = {'symbol': symbol,
              'period': period,
              'size': size}

    url = MARKET_URL + '/market/history/kline'
    return http_get_request(url, params)


# 获取marketdepth
def get_depth(symbol, type):
    """
    :param symbol: 
    :param type: 可选值：{ percent10, step0, step1, step2, step3, step4, step5 }
    :return:
    """
    params = {'symbol': symbol,
              'type': type}

    url = MARKET_URL + '/market/depth'
    return http_get_request(url, params)


# 获取tradedetail
def get_trade(symbol):
    """
    :param symbol: 可选值：{ ethcny }
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/trade'
    return http_get_request(url, params)


# 获取 Market Detail 24小时成交量数据
def get_detail(symbol):
    """
    :param symbol: 可选值：{ ethcny }
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail'
    return http_get_request(url, params)


# 查询系统支持的所有交易对


def get_symbols():
    """
    :return:
    """
    url = MARKET_URL + '/v1/common/symbols'
    params = {}
    return http_get_request(url, params)

if __name__ == '__main__':
    print(get_symbols())