# -*- coding: utf-8 -*-

from logger import Logger
from service_binance import *
from util_array import Array
import numpy as np
from decimal import Decimal


class Binance:
    def __init__(self):
        self.logging = Logger().get_log()

    def get_coin_price_api(self, symbol):
        """
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
        symbol 默认请求格式 eth_usdt（统一），huobi实际查询 ethusdt
        symbol处理逻辑如下：
        1. 如果是usdt结尾，直接查询
        2. 如果不是usdt 结尾，是eth、btc结尾 直接查询
        3. 如果不是usdt结尾，且不是eth、btc结尾,或者==eth == btc,均当作usdt 交易对处理，程序自动加上usdt进行查询

        最后统一 大写，然后替换下划线
        """
        # self.logging.info('binance query:%s', symbol)
        # symbol = symbol.lower(symbol.strip(symbol))
        symbol = symbol.strip().lower()
        coin_market = symbol
        if ('eth' == symbol or 'btc' == symbol) or (
                not (symbol.endswith('usdt') or symbol.endswith('eth') or symbol.endswith('btc'))):
            # 当作usdt 交易对处理，程序自动加上usdt进行查询
            coin_market = symbol + 'usdt'

        # 币安交易对都是大写
        objs = get_price(coin_market.upper().replace('_', ''))
        """
        {
          "symbol": "LTCBTC",
          "price": "4.00000200"
        }
        """
        _map = "交易所:\tbinance\n交易对:\t%s" % coin_market

        if objs:
            if ('status' in objs) and (objs['status'] != 'ok'):
                return 'cannot query the price of %s from binance' % coin_market
            if 'msg' in objs and 'code' in objs:
                return 'cannot query the price of %s from binance, msg=%s' % (coin_market, objs['msg'])
            jsonobj = objs
            if 'price' in jsonobj:
                _tmp = "\n当前价: \t%s" % jsonobj['price']
                _map = _map + _tmp
            return _map
        else:
            return "cannot query the price of %s from binance" % coin_market

    def get_coin_depth(self, symbol, limit=50):

        objs = get_depth(symbol.strip().upper().replace('_', ''), limit)
        """
        {
            "lastUpdateId": 131864463,
            "bids": [
                ["0.08458400", "0.94600000", []],
                ["0.08456600", "0.50000000", []],
                ["0.08455900", "7.50300000", []],
                ["0.08455800", "1.01300000", []],
                ["0.08455700", "0.52300000", []]
            ],
            "asks": [
                ["0.08459900", "0.44300000", []],
                ["0.08460000", "2.61800000", []],
                ["0.08462300", "0.48300000", []],
                ["0.08462700", "0.02000000", []],
                ["0.08463100", "0.40000000", []]
            ]
        }
        """
        _len = len(objs['bids'])
        bids = Array(objs['bids'])
        asks = Array(objs['asks'])
        bid_one = objs['bids'][0][0]
        ask_one = objs['asks'][0][0]
        bids_numbs = bids[0:_len, 1:2]
        asks_numbs = asks[0:_len, 1:2]
        sum_bids = 0.0
        for _item in bids_numbs:
            sum_bids = Decimal(str(sum_bids)) + Decimal(_item[0])

        sum_asks = 0.0
        for _item in asks_numbs:
            sum_asks = Decimal(str(sum_asks)) + Decimal(_item[0])

        # _return_map = dict()
        #
        # _return_map['买单数:'] = str(sum_bids)
        # _return_map['卖单数:'] = str(sum_asks)
        # _return_map['买一价:'] = bid_one
        # _return_map['卖一价:'] = ask_one
        # print(_return_map)

        _map = u"交易所:\t%s\n 交易对:\t%s\n 买单数:\t%s\n 卖单数:\t%s\n 买一价:\t%s\n 卖一价:\t%s" % (
        '币安', symbol, str(sum_bids), str(sum_asks), bid_one, ask_one)
        #print(_map)
        return _map


# Binance().get_coin_depth('EOS_BTC', 50)
