from redisservice import cache
from tools import http_get_request
from logger import Logger
from config import OK_COIN_MARKET_USDT
import string
import time



class OKEX:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = 'https://www.okex.com/api/v1/ticker.do'

    # @cache
    def get_coin_price_api(self, symbol):
        #_symbol = symbol.upper(symbol.strip(symbol))
        _symbol = symbol.strip().upper()
        coin_market = OK_COIN_MARKET_USDT.get(_symbol)
        _data = {'symbol': _symbol}
        if coin_market:
            _symbol = coin_market
            _data = {'symbol': coin_market}
        objs = http_get_request(self.homeUrl, _data)

        """
        {
            "date":"1410431279",
            "ticker":{
                "buy":"33.15",
                "high":"34.15",
                "last":"33.15",
                "low":"32.05",
                "sell":"33.16",
                "vol":"10532696.39199642"
            }
        }
        """
        _map = " exchange:okex\n symbol:%s" % _symbol

        if objs:
            if ('status' in objs) and (objs['status'] != 'ok'):
                return 'cannot query the price of %s from okex' % coin_market
            if 'ticker' in objs:
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
                    _map = _map + "\n time:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(long(_time))))
                return _map
            return "cannot query the price of %s from okex" % _symbol
        else:
            return "cannot query the price of %s from okex" % _symbol

# print OKEX().get_coin_price_api('eth')
