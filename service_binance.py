# -*- coding: utf-8 -*-
from config import BA_MARKET_URL
from util_tools import http_get_request

# 获取tradedetail
def get_price(symbol):
    """
    :param symbol: symbol	STRING 全大写
    :return:
    """
    params = {'symbol': symbol}

    url = BA_MARKET_URL + '/api/v3/ticker/price'
    return http_get_request(url, params)
