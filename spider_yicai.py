# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from util_tools import get_request
from util_tools import html_replace_char
from logger import Logger
from config import SPD_YICAI_URL
from config import DEFAULT_ENCODING
from service_spider_common import filter_news
from service_spider_common import save_cursor

class SpiderYiCai:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = SPD_YICAI_URL
        self.encoding = DEFAULT_ENCODING
        self.redis_key = 'yicai'

    def get_news(self):
        response = get_request(self.homeUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        _article_list = soup.select('div #news_List > dl')[:5]

        _allow_return_list = []
        _article_cursor = []
        for item in _article_list:
            _article = self._handle_article_item(item)
            _article_cursor.append(int(_article['_cursor']))
            # print(int(_article['_cursor']))
            # print(_article['title'])
            if filter_news(self.redis_key, _article):
                _allow_return_list.append(_article)
        # print('max ----- %d' % max(_article_cursor))
        save_cursor(self.redis_key, max(_article_cursor))
        return _allow_return_list

    @staticmethod
    def _handle_article_item(article_item):
        try:
            _article = {}
            _atc_url = article_item.select('h3 > a')[0]
            _atc_remark = article_item.find('h4')
            _atc_desc = article_item.find('p')
            _article['_type'] = 'news'
            _article['_source'] = 'yicai'
            _article['url'] = _atc_url['href']
            _article['title'] = _atc_url.get_text().replace("\n", "").encode(_DEFAULT_ENCODING)
            _article['remark'] = _atc_remark.get_text().replace('span', '').replace('>', ' ').replace("<", "").encode(_DEFAULT_ENCODING)
            _article['desc'] = html_replace_char(_atc_desc.get_text().replace("\n", "")).encode(_DEFAULT_ENCODING)

            # http://www.yicai.com/news/5401850.html
            _start = _article['url'].rindex('/') + 1
            _end = len(_article['url']) - 5
            _last_index = _article['url'][_start:_end]
            _article['_cursor'] = _last_index
            return _article
        except Exception:
            return None


# SpiderYiCai().get_news()