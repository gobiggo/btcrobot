# -*- coding: utf-8 -*-

from util_tools import get_request
from logger import Logger
from config import SPD_WALLS_CN_LIVE_URL
from config import DEFAULT_ENCODING
from service_spider_common import filter_live
from service_spider_common import save_cursor

class SpiderWallsLive:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = SPD_WALLS_CN_LIVE_URL
        self.encoding = DEFAULT_ENCODING
        self.redis_key = 'wallstreetcn_live'

    def get_news(self):
        # https://api-prod.wallstreetcn.com/apiv1/content/lives?channel=blockchain-channel&limit=1
        response = get_request(self.homeUrl)
        jsonobj = response.json()
        """
        {
            "code": 20000,
            "message": "OK",
            "data": {
                "items": [{
                    "article": null,
                    "author": {
                        "id": 0,
                        "display_name": "",
                        "image": "",
                        "uri": ""
                    },
                    "channels": ["a-stock-channel", "blockchain-channel"],
                    "content": "【挖矿公司比特大陆去年利润超30亿美元，与美国半导体巨头英伟达相当】日前投行伯恩斯坦（Bernstein）分析师根据对75％的毛利率和65％的经营利润率的保守预期，在比特币“挖矿”行业中占据着主导地位的比特大陆（Bitmain），2017年的营业利润为30亿美元至40亿美元。而据估计，同期的Nvidia营运利润为30亿美元。",
                    "content_more": "",
                    "content_text": "【挖矿公司比特大陆去年利润超30亿美元，与美国半导体巨头英伟达相当】日前投行伯恩斯坦（Bernstein）分析师根据对75％的毛利率和65％的经营利润率的保守预期，在比特币“挖矿”行业中占据着主导地位的比特大陆（Bitmain），2017年的营业利润为30亿美元至40亿美元。而据估计，同期的Nvidia营运利润为30亿美元。",
                    "display_time": 1519566039,
                    "global_channel_name": "7x24快讯",
                    "global_more_uri": "wscn://wallstreetcn.com/live",
                    "id": 1161517,
                    "image_uris": [],
                    "is_favourite": false,
                    "reference": "",
                    "score": 1,
                    "symbols": [],
                    "tags": [],
                    "title": ""
                }],
                "next_cursor": "1519566039",
                "polling_cursor": "1161517"
            }
        }
        """
        if jsonobj and ('message' in jsonobj) and (jsonobj['message'] == 'OK'):
            _article_list = jsonobj['data']['items']
            _allow_return_list = []
            _article_cursor = []
            for item in _article_list:
                _article = self._handle_article_item(item)
                _article_cursor.append(int(_article['_cursor']))
                #print(int(_article['_cursor']))
                #print(_article['desc'])
                if filter_live(self.redis_key, _article):
                    # print(_article['desc'])
                    _allow_return_list.append(_article)
            # print('max ----- %d' % max(_article_cursor))

            save_cursor(self.redis_key, max(_article_cursor))
            return _allow_return_list

    @staticmethod
    def _handle_article_item(article_item):
        try:
            _article = {}

            _article['_type'] = 'live'
            _article['_source'] = 'wallstreetcn_live'
            _article['url'] = None
            _article['title'] = None
            _article['remark'] = None
            _article['desc'] = article_item['content']
            _article['time'] = article_item['display_time']

            _article['_cursor'] = article_item['id']
            return _article
        except Exception as e:
            print(e)
            return None


# SpiderWallsLive().get_news()
