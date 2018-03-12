from util_tools import Tools
from logger import Logger
from config import ZB_COIN_MARKET_USDT
from config import ZB_API_URL
import time


class ZB:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = ZB_API_URL

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
        _map = "交易所:\tzb\n 交易对:\t%s" % _symbol

        if objs and ('ticker' in objs):
            jsonobj = objs['ticker']
            if 'last' in jsonobj:
                _tmp = "\n 当前价:\t%s" % jsonobj['last']
                _map = _map + _tmp
            if 'buy' in jsonobj:
                _tmp = "\n 买一价:\t%s" % jsonobj['buy']
                _map = _map + _tmp
            if 'sell' in jsonobj:
                _tmp = "\n 卖一价:\t%s" % jsonobj['sell']
                _map = _map + _tmp
            if 'high' in jsonobj:
                _tmp = "\n 24h最高:\t%s" % jsonobj['high']
                _map = _map + _tmp
            if 'low' in jsonobj:
                _tmp = "\n 24h最低:\t%s" % jsonobj['low']
                _map = _map + _tmp
            if 'vol' in jsonobj:
                _tmp = "\n 24h交易:\t%s 个" % jsonobj['vol']
                _map = _map + _tmp

            if 'date' in objs:
                _time = objs['date']
                _map = _map + "\n #时间:\t%s" % (time.strftime("%H:%M:%S", time.localtime(int(_time))))
            return _map
        else:
            return "cannot query the price of %s from zb" % _symbol

# print ZB().get_coin_price_api('bts')
