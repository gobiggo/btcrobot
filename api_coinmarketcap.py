from util_tools import Tools
from util_tools import get_request
from logger import Logger
from config import COIN_SYMBOL_ID
from config import CMC_API_URL
import time


class CoinMarketCap:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = CMC_API_URL

    def get_coin_global_api(self, convert='USD'):
        _url = self.homeUrl + "global"
        if convert:
            _url = self.homeUrl + "global/?convert=%s"
        objs = get_request(_url).text()
        """
        {
            "total_market_cap_usd": 453165692235.0, 
            "total_24h_volume_usd": 19241568080.0, 
            "bitcoin_percentage_of_market_cap": 38.73, 
            "active_currencies": 902, 
            "active_assets": 589, 
            "active_markets": 8791, 
            "last_updated": 1519717469
        }
        """
        return objs.replace("{", "").replace("}", "").replace(',', '\n')

    def get_coin_price_api(self, symbol):
        # coin_id = COIN_SYMBOL_ID.get(symbol.upper(symbol.strip(symbol)))
        coin_id = COIN_SYMBOL_ID.get(symbol.strip().upper())
        _url = self.homeUrl + "ticker/" + symbol
        if coin_id:
            _url = self.homeUrl + coin_id

        objs = Tools().request(_url)
        """
        [{
            "id": "bitcoin", 
            "name": "Bitcoin", 
            "symbol": "BTC", 
            "rank": "1", 
            "price_usd": "10667.8", 
            "price_btc": "1.0", 
            "24h_volume_usd": "8203140000.0", 
            "market_cap_usd": "180068463575", 
            "available_supply": "16879625.0", 
            "total_supply": "16879625.0", 
            "max_supply": "21000000.0", 
            "percent_change_1h": "-1.04", 
            "percent_change_24h": "-5.07", 
            "percent_change_7d": "9.23", 
            "last_updated": "1519289669"
        }]
        """
        _map = " exchange:\tCoinMarketCap"
        if (objs is not None) and len(objs) > 0:
            jsonobj = objs[0]
            if 'symbol' in jsonobj:
                _tmp = "\n ...symbol:\t%s" % jsonobj['symbol']
                _map = _map + _tmp
            if 'price_usd' in jsonobj:
                _tmp = "\n price_usd:\t%s" % jsonobj['price_usd']
                _map = _map + _tmp
            if 'price_btc' in jsonobj:
                _tmp = "\n price_btc:\t%s" % jsonobj['price_btc']
                _map = _map + _tmp
            if 'percent_change_1h' in jsonobj:
                _tmp = "\n change_1h:\t%.2f%%" % float(jsonobj['percent_change_1h'])
                _map = _map + _tmp
            if 'percent_change_24h' in jsonobj:
                _tmp = "\n change_1d:\t%.2f%%" % float(jsonobj['percent_change_24h'])
                _map = _map + _tmp
            if 'percent_change_7d' in jsonobj:
                _tmp = "\n change_7d:\t%.2f%%" % float(jsonobj['percent_change_7d'])
                _map = _map + _tmp
            if 'last_updated' in jsonobj:
                _tmp = "\n last_time:\t%s" % (time.strftime("%H:%M:%S", time.localtime(int(jsonobj['last_updated']))))
                _map = _map + _tmp
            return _map

        else:
            return "cannot query the price of %s (query by coin-id,not symbol) from CoinMarketCap" % symbol

# print CoinMarketCap().get_coin_price_api('verge')
