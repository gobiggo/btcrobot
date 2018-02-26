# -*- coding: utf-8 -*-

from service_mail import MailService
from spider_wallstreetcn_live import SpiderWallsLive

_lives = SpiderWallsLive().get_news()

MailService().send_live_email(_lives)
