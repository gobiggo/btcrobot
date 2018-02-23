# -*- coding: utf-8 -*-

import sys

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

# btc_usdt eth_usdt ltc_usdt etc_usdt bch_usdt qtum_usdt hsr_usdt neo_usdt gas_usdt
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

EXCHANGES = ('HB', 'BA', 'OK', 'ZB','CMC')

BA_MARKET_URL = 'https://api.binance.com'

# huobi API 请求地址
HB_API_HOST = "https://api.huobi.pro"
HB_MARKET_URL = HB_TRADE_URL = "https://api.huobi.pro"