# -*- coding: utf-8 -*-

from logger import Logger
import time
from service_huobi import *


class HuoBi:
    def __init__(self):
        self.logging = Logger().get_log()

    def get_coin_price_api(self, symbol):
        # https://api.huobi.pro/market/trade?symbol=ethusdt
        """
        symbol 默认请求格式 eth_usdt（统一），huobi实际查询 ethusdt
        symbol处理逻辑如下：
        1. 如果是usdt结尾，直接查询
        2. 如果不是usdt 结尾，是eth、btc结尾 直接查询
        3. 如果不是usdt结尾，且不是eth、btc结尾,或者==eth == btc,均当作usdt 交易对处理，程序自动加上usdt进行查询
        
        最后统一替换下划线
        """

        # symbol = symbol.lower(symbol.strip(symbol))
        symbol = symbol.strip().lower()
        coin_market = symbol
        if ('eth' == symbol or 'btc' == symbol) or (not (symbol.endswith('usdt') or symbol.endswith('eth') or symbol.endswith('btc'))):
            # 当作usdt 交易对处理，程序自动加上usdt进行查询
            coin_market = symbol + 'usdt'

        #print coin_market
        objs = get_trade(coin_market.replace('_', ''))
        #print objs

        """
        {
            "status": "ok",
            "ch": "market.ethusdt.trade.detail",
            "ts": 1519369668626,
            "tick": {
                "id": 2884782585,
                "ts": 1519369666954,
                "data": [{
                    "amount": 0.014500000000000000,
                    "ts": 1519369666954,
                    "id": 28847825851753558255,
                    "price": 834.160000000000000000,
                    "direction": "sell"
                }, {
                    "amount": 0.823000000000000000,
                    "ts": 1519369666954,
                    "id": 28847825851753556144,
                    "price": 833.990000000000000000,
                    "direction": "sell"
                }]
            }
        }}
        """
        _map = "交易所:\thuobi\n 交易对:\t%s" % coin_market

        if objs and ('status' in objs):
            if objs['status'] != 'ok':
                if 'err-msg' in objs:
                    return 'cannot query the price of %s from huobi,error-msg: %s' % (coin_market, objs['err-msg'])
                return 'query %s failed' % coin_market
            if 'tick' not in objs:
                return 'query %s failed' % coin_market
            ticker = objs['tick']
            if 'data' not in ticker or (len(ticker['data']) <= 0):
                return 'query %s failed' % coin_market
            jsonobj = ticker['data'][0]
            if 'price' in jsonobj:
                _tmp = "\n 当前价:\t%s" % jsonobj['price']
                _map = _map + _tmp
            if 'amount' in jsonobj:
                _tmp = "\n 交易数:\t%s" % jsonobj['amount']
                _map = _map + _tmp
            if 'ts' in jsonobj:
                _time = jsonobj['ts']
                _map = _map + ("\n #时间:\t%s" % (time.strftime("%H:%M:%S", time.localtime(int(_time) / 1000))))
            return _map
        else:
            return "cannot query the price of %s from huobi" % coin_market


# print HuoBi().get_coin_price_api('nas')
