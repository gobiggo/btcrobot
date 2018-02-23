# -*- coding: utf-8 -*-

"""
https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
@QQ      : 583748826
"""
from redisservice import cache
from logger import Logger
import string
from binance_service import *

class Binance:
    def __init__(self):
        self.logging = Logger().get_log()

    # @cache
    def get_coin_price_api(self, symbol):
        """
        symbol 默认请求格式 eth_usdt（统一），huobi实际查询 ethusdt
        symbol处理逻辑如下：
        1. 如果是usdt结尾，直接查询
        2. 如果不是usdt 结尾，是eth、btc结尾 直接查询
        3. 如果不是usdt结尾，且不是eth、btc结尾,或者==eth == btc,均当作usdt 交易对处理，程序自动加上usdt进行查询

        最后统一 大写，然后替换下划线
        """

        # symbol = symbol.lower(symbol.strip(symbol))
        symbol = symbol.strip().lower()
        coin_market = symbol
        if ('eth' == symbol or 'btc' == symbol) or (
        not (symbol.endswith('usdt') or symbol.endswith('eth') or symbol.endswith('btc'))):
            # 当作usdt 交易对处理，程序自动加上usdt进行查询
            coin_market = symbol + 'usdt'

        # print coin_market
        # 币安交易对都是大写
        objs = get_price(coin_market.upper().replace('_', ''))
        # print objs

        """
        {
          "symbol": "LTCBTC",
          "price": "4.00000200"
        }
        """
        _map = " exchange:binance\n symbol:%s" % coin_market

        if objs:
            if ('status' in objs) and (objs['status'] != 'ok'):
                return 'cannot query the price of %s from binance' % coin_market
            if 'msg' in objs and 'code' in objs :
                return 'cannot query the price of %s from binance, msg=%s' % (coin_market,objs['msg'])
            jsonobj = objs
            if 'price' in jsonobj:
                _tmp = "\n price:%s" % jsonobj['price']
                _map = _map + _tmp
            return _map
        else:
            return "cannot query the price of %s from binance" % coin_market


# print Binance().get_coin_price_api('xvgeth')
