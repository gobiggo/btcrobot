# -*- coding: utf-8 -*-

import json
from bs4 import BeautifulSoup
from util_tools import get_request
from util_tools import html_replace_char
from logger import Logger
from config import SPD_CAIXIN_URL
from config import DEFAULT_ENCODING


class Spider_Caixin:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = SPD_CAIXIN_URL
        self.encoding = DEFAULT_ENCODING

    def get_news(self):
        response = get_request(self.homeUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        _article_list = soup.select('div #listArticle > div[class*=boxa]')

        _allow_return_list = []
        _i
        for item in _article_list:
            _article = self._handle_article_item(item)
            print(_article)
            # 1. _cursor > history_index
            # 2. desc 含 关键词

    @staticmethod
    def _handle_article_item(article_item):
        try:
            _article = {}
            _atc_url = article_item.select('h4 > a')[0]
            _atc_remark = article_item.find('span')
            _atc_desc = article_item.find('p')
            _article['_type'] = 'news'
            _article['_source'] = 'caixin'
            _article['url'] = _atc_url['href']
            _article['title'] = _atc_url.get_text().replace("\n", "")
            _article['remark'] = _atc_remark.get_text().replace("\n", "")
            _article['desc'] = html_replace_char(_atc_desc.get_text().replace("\n", ""))

            # finance.caixin.com/2018-02-24/101213298.html 取 101213298
            _start = _article['url'].rindex('/') + 1
            _end = len(_article['url']) - 5
            _last_index = _article['url'][_start:_end]
            _article['_cursor'] = _last_index
            return _article
        except Exception:
            return None


print(Spider_Caixin().get_news())
