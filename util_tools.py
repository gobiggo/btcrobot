# -*- coding: utf-8 -*-

import urllib
import socket
import json
from logger import Logger
import requests
from urllib.parse import urlencode, quote_plus
import re

# timeout in 5 seconds:
TIMEOUT = 10

SCHEME = 'https'

# language setting: 'zh-CN', 'en':
LANG = 'zh-CN'

DEFAULT_GET_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': LANG,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
}

DEFAULT_POST_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Language': LANG,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
}


# 各种请求,获取数据方式
def get_request(url, params=None, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    try:
        response = requests.get(url, params, headers=headers, timeout=TIMEOUT)
        return response
    except Exception as e:
        print("httpGet failed, detail is:%s" % e)
        return "fail"


def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = urlencode(params, quote_via=quote_plus)
    try:
        response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        return response.json()
        # if response.status_code == 200:
        #     return response.json()
        # else:
        #     return {"status":"fail"}
    except Exception as e:
        print("httpGet failed, detail is:%s" % e)
        return {"status": "fail", "msg": e}


def http_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        "User-Agent": "Chrome/39.0.2171.71",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = json.dumps(params)
    try:
        response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print("httpPost failed, detail is:%s" % e)
        return {"status": "fail", "msg": e}


# 用 非贪婪模式 匹配 \t 或者\n 或者 空格超链接 和图片
BgnCharToNoneRex = re.compile("(\t|\n|\r| |<a.*?>|<img.*?>)")  # 用 非贪婪模式 陪 任意 <>
EndCharToNoneRex = re.compile("<.*?>")

# 用 非贪婪模式匹配 任意 <p> 标签
BgnPartRex = re.compile("<p.*?>")
CharToNewLineRex = re.compile("(<br />|</p>|<tr>|<div>|</div>)")
CharToNewTabRex = re.compile("<td>")

# 将一些html符号尸体转变为原始符号
replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]


def html_replace_char(x):
    x = BgnCharToNoneRex.sub("", x)
    x = BgnPartRex.sub("\n    ", x)
    x = CharToNewLineRex.sub("\n", x)
    x = CharToNewTabRex.sub("\t", x)
    x = EndCharToNoneRex.sub("", x)

    for t in replaceTab:
        x = x.replace(t[0], t[1])
    return x


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

class Tools:
    def __init__(self):
        self.logging = Logger().get_log()
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}

    def request(self, url, query_object=None):
        self.logging.info("request url:%s", url)
        _data = None
        if query_object is not None:
            _data = urlencode(query_object, quote_via=quote_plus)
        try:
            response = requests.get(url, _data, headers=self.headers, timeout=TIMEOUT).json()
        except urllib.error.HTTPError as e:
            error_message = e.read()
            if error_message:
                self.logging.error("===request error,error_message:%s", error_message)
            elif hasattr(e, "code") and hasattr(e, "reason"):
                self.logging.error("===request error,code:%s;reason:%s", e.code, e.reason)
            else:
                self.logging.error("===request error")
            return None
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                self.logging.error("===request error,request timeout")
            else:
                if hasattr(e, "code") and hasattr(e, "reason"):
                    self.logging.error("===request error,code:%s;reason:%s", e.code, e.reason)
                else:
                    self.logging.error("===request error")
            return None
        return response
