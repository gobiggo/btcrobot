# -*- coding: utf-8 -*-
from robot_coin import auto_query_coin_price


def printx(msg):
    print('-----------\n %s' % msg)


def test():
    printx(auto_query_coin_price(':help'))
    printx(auto_query_coin_price(':BTC/CMC'))
    printx(auto_query_coin_price(':NAS/hb'))
    printx(auto_query_coin_price(':btc_usdt/ba'))
    printx(auto_query_coin_price(':eos/ok'))
    printx(auto_query_coin_price(':NASETH/HB'))
    printx(auto_query_coin_price(':naseth/hb'))
    printx(auto_query_coin_price(':bts_BTC/ZB'))
    print('----------------None or Exception----------')
    printx(auto_query_coin_price(':EOS_BC/BA'))
    printx(auto_query_coin_price(':EOSBTC/'))
    printx(auto_query_coin_price(':/EOSBTC/OK'))
    printx(auto_query_coin_price('help'))
    printx(auto_query_coin_price(':NASETH/HB/DEPTH'))
    printx(auto_query_coin_price(':中文试试'))

def testx():
    printx(auto_query_coin_price(':help'))
    printx(auto_query_coin_price(':ETH'))

testx()