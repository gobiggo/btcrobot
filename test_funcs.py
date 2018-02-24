# -*- coding: utf-8 -*-


def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)


symbol = 'EOSBTC/BA/PRICE'
symbol2 = 'EOSBTC/BA/PRICE 中文'


print(judge_pure_english(symbol))
print(judge_pure_english(symbol2))

