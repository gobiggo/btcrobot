from redisservice import cache
from tools import Tools
from logger import Logger
from config import ZB_COIN_MARKET_USDT
import string
import time


class ZB:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = 'http://api.zb.com/data/v1/ticker'

    # @cache
    def get_coin_price_api(self, symbol):
        # http://api.zb.com/data/v1/ticker?market=btc_usdt
        _symbol = symbol.strip().upper()
        coin_market = ZB_COIN_MARKET_USDT.get(_symbol)
        _data = {'market': _symbol}
        if coin_market:
            _data = {'market': coin_market}
        objs = Tools().request(self.homeUrl, _data)

        """
        {
            "ticker": {
                "vol": "2681.2393",
                "last": "9925.0",
                "sell": "9924.7",
                "buy": "9921.45",
                "high": "10979.99",
                "low": "9866.03"
            },
            "date": "1519355461791"
        }
        """
        _map = " exchange:zb\n symbol:%s" % coin_market

        if objs and ('ticker' in objs):
            jsonobj = objs['ticker']
            if 'last' in jsonobj:
                _tmp = "\n price:%s" % jsonobj['last']
                _map = _map + _tmp
            if 'buy' in jsonobj:
                _tmp = "\n buy:%s" % jsonobj['buy']
                _map = _map + _tmp
            if 'sell' in jsonobj:
                _tmp = "\n sell:%s" % jsonobj['sell']
                _map = _map + _tmp
            if 'high' in jsonobj:
                _tmp = "\n high_24h:%s" % jsonobj['high']
                _map = _map + _tmp
            if 'low' in jsonobj:
                _tmp = "\n low_24h:%s" % jsonobj['low']
                _map = _map + _tmp
            if 'vol' in jsonobj:
                _tmp = "\n vol_24h:%s" % jsonobj['vol']
                _map = _map + _tmp

            if 'date' in objs:
                _time = objs['date']
                _map = _map + "\n time:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(long(_time)/1000)))
            return _map
        else:
            return "cannot query the price of %s from zb" % _symbol

# print ZB().get_coin_price_api('bts')
