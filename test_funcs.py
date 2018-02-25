# -*- coding: utf-8 -*-


def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)


symbol = 'EOSBTC/BA/PRICE'
symbol2 = 'EOSBTC/BA/PRICE 中文'

print(symbol.rindex('/'))
print(symbol.index('/'))
print(judge_pure_english(symbol))
print(judge_pure_english(symbol2))

_article = {}
_article['url'] = 'https://finance.caixin.com/2018-02-24/101213298.html'
_start = _article['url'].rindex('/')+1
_end = len(_article['url']) - 5
_last_index = _article['url'][_start:_end]

print(_last_index)
