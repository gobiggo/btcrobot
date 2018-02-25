# -*- coding: utf-8 -*-

import json
from util_tools import get_request
from util_tools import html_replace_char
from logger import Logger
from config import WALLS_CN_URL
from config import DEFAULT_ENCODING


class Spider_Walls:
    def __init__(self):
        self.logging = Logger().get_log()
        self.homeUrl = WALLS_CN_URL
        self.encoding = DEFAULT_ENCODING

    def get_news(self):
        # https://api-prod.wallstreetcn.com/apiv1/content/articles?
        # category=global&limit=20&cursor=1519530709,1519473979&platform=wscn-platform
        response = get_request(self.homeUrl)
        jsonobj = response.json()
        """
        {"code":20000
        ,"message":"OK"
        ,"data":
            {"items":
                [{"author":{"avatar":"https://wpimg.wallstcn.com/ivanka_avatar_10.png","display_name":"张超","id":120000000921,"uri":"https://wallstreetcn.com/authors/120000000921"}
                ,"categories":["global","china","enterprise","tmt-carousel","tmt-fintech","tmt-firm"]
                ,"comment_count":0
                ,"content_short":"嘉楠耘智发明了中国第一台比特币矿机——“阿瓦隆”，截至2017年4"
                ,"display_time":1519530709
                ,"external":false
                ,"id":3237965
                ,"image_uri":"https://wpimg.wallstcn.com/6ef30070-c53b-4676-b1c2-2c2785bc49a3.jpg"
                ,"is_paid":false,"is_priced":false,"is_trial":false,"layout":"tech-layout","pageviews":672,"platforms":["tech-platform","wscn-platform"],"related_topics":[]
                ,"source_name":""
                ,"source_uri":"https://awtmt.com/articles/3237965?from=wscn"
                ,"symbols":[],"tags":[]
                ,"title":"嘉楠耘智孔剑平揭秘：世界第二大比特币矿机生产商是如何炼成的"
                ,"unshow_content_short":false
                ,"uri":"https://wallstreetcn.com/articles/3237965"}]
                ,"next_cursor":"1519530709,1519530709"}}
        """
        if jsonobj and ('message' in jsonobj) and (jsonobj['message'] == 'OK'):
            _article_list = jsonobj['data']['items']
            for item in _article_list:
                _article = self._handle_article_item(item)
                print(_article)
            #

    @staticmethod
    def _handle_article_item(article_item):
        try:
            _article = {}

            _article['_type'] = 'article'
            _article['_source'] = 'wallstreetcn'
            _article['url'] = article_item['uri']
            _article['title'] = article_item['title']
            _article['remark'] = None
            _article['desc'] = article_item['content_short']
            _article['time'] = article_item['display_time']

            # finance.caixin.com/2018-02-24/101213298.html 取 101213298
            _article['_cursor'] = article_item['display_time']
            return _article
        except Exception:
            return None


print(Spider_Walls().get_news())