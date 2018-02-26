# -*- coding: utf-8 -*-

from service_mail import MailService
from spider_caix import SpiderCaixin
from spider_wallstreetcn import SpiderWalls

_articles1 = SpiderCaixin().get_news()
_articles2 = SpiderWalls().get_news()

_articles1.extend(_articles2)

MailService().send_email(_articles1)
