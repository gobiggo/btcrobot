# -*- coding: utf-8 -*-

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

EMAIL_RECEIVERS = ['583748826@qq.com']
EMAIL_SENDER = 'sloong@yeah.net'
EMAIL_PWD = 'po000po000'
EMAIL_SMTP = 'smtp.yeah.net'

EXCHANGES = ('HB', 'BA', 'OK', 'ZB', 'CMC')
FUNCTIONS = ('DEPTH', 'KLINE', 'GLOBAL')

BA_MARKET_URL = 'https://api.binance.com'

# huobi API 请求地址
HB_API_HOST = HB_MARKET_URL = HB_TRADE_URL = "https://api.huobi.pro"

# zb.com API地址
ZB_API_URL = 'http://api.zb.com/data/v1/ticker'

# CMC API地址
CMC_API_URL = 'https://api.coinmarketcap.com/v1/'

# OK API 地址
OK_API_URL = 'https://www.okex.com/api/v1/ticker.do'

# CMC SYMBOL_ID 对应关系（部分
COIN_SYMBOL_ID = {"BTC": "bitcoin"
    , "ETH": "ethereum"
    , "XRP": "ripple"
    , "BCH": "bitcoin-cash"
    , "LTC": "litecoin"
    , "NEO": "neo"
    , "EOS": "eos"
    , "DASH": "dash"
    , "QTUM": "qtum"
    , "ETC": "ethereum-classic"}

# ZB SYMBOL_USDT 对应关系
ZB_COIN_MARKET_USDT = {"BTC": "btc_usdt"
    , "ETH": "eth_usdt"
    , "XRP": "xrp_usdt"
    , "BCH": "bch_usdt"
    , "LTC": "ltc_usdt"
    , "HSR": "hsr_usdt"
    , "EOS": "eos_usdt"
    , "DASH": "dash_usdt"
    , "QTUM": "qtum_usdt"
    , "ETC": "etc_usdt"
    , "BTS": "bts_usdt"}

# OK SYMBOL_USDT 对应关系
OK_COIN_MARKET_USDT = {"BTC": "btc_usdt"
    , "ETH": "eth_usdt"
    , "XRP": "xrp_usdt"
    , "BCH": "bch_usdt"
    , "LTC": "ltc_usdt"
    , "HSR": "hsr_usdt"
    , "EOS": "eos_usdt"
    , "DASH": "dash_usdt"
    , "QTUM": "qtum_usdt"
    , "ETC": "etc_usdt"
    , "NEO": "neo_usdt"
    , "GAS": "gas_usdt"}

# huobi SYMBOL_USDT 对应关系
HB_COIN_MARKET_USDT = {"BTC": "btc_usdt"
    , "ETH": "eth_usdt"
    , "XRP": "xrp_usdt"
    , "BCH": "bch_usdt"
    , "LTC": "ltc_usdt"
    , "HSR": "hsr_usdt"
    , "EOS": "eos_usdt"
    , "DASH": "dash_usdt"
    , "QTUM": "qtum_usdt"
    , "ETC": "etc_usdt"
    , "OMG": "omg_usdt"
    , "ZEC": "zec_usdt"
    , "ITC": "itc_usdt"
    , "NAS": "nas_usdt"
    , "NEO": "neo_usdt"
    , "XEM": "xem_usdt"
    , "BTS": "bts_usdt"}

# -------- spider -------
FILTER_KEYWORDS = (
    '比特', '区块', '链圈', '代币', '数字资产', '数字货币', '虚拟货币', '加密货币', '山寨币', 'ico', 'ICO', 'btc', 'bitcoin', 'BTC', 'BITCOIN')

DEFAULT_ENCODING = 'utf-8'

# caixin.com
SPD_CAIXIN_URL = 'http://finance.caixin.com/'

# yicai
SPD_YICAI_URL = 'http://www.yicai.com/news/jinrong/'

# wallstreetcn
SPD_WALLS_CN_URL = 'https://api-prod.wallstreetcn.com/apiv1/content/articles?category=global&limit=5'
SPD_WALLS_CN_LIVE_URL = 'https://api-prod.wallstreetcn.com/apiv1/content/lives?channel=blockchain-channel&limit=5'

# cailianpress
SPD_CAILIAN_URL = 'https://www.cailianpress.com/'

# pbc
SPD_PBC_URL = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html'
