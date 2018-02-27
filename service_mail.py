# -*- coding: utf-8 -*-

import smtplib
from smtplib import SMTPException
# from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config import EMAIL_RECEIVERS
from config import EMAIL_SENDER
from config import EMAIL_SMTP
from config import EMAIL_PWD
from util_tools import singleton
from logger import Logger
from api_binance import get_price


def _format_addr(s):
    name, _addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), _addr))


@singleton
class MailService:
    def __init__(self):
        self.news_template = "<p><a href='%s'>%s</a><br/>[%s] %s</p>"
        self.live_template = "<p>%s</p>"
        self.html_template = "<html><body>%s<div>+微信：shuishuile</div></body></html>"
        self.logger = Logger().get_log()

    def send_email(self, _articles=None):
        if _articles and len(_articles) > 0:
            _receivers = ','.join(EMAIL_RECEIVERS)
            # print(_receivers)
            html_msg = self.build_up_html(_articles)
            # print(html_msg)

            jsonobj = get_price("BTCUSDT")
            btc_price = jsonobj['price']

            msg = MIMEText(html_msg, 'html', 'utf-8')
            msg['From'] = _format_addr('共 %d 条新闻，敬请查看 <%s>' % (len(_articles), EMAIL_SENDER))
            msg['To'] = _format_addr('收件人 <%s>' % _receivers[0])
            msg['Subject'] = Header("币安BTC当前报价:%s" % btc_price, 'utf-8').encode()
            try:
                server = smtplib.SMTP(EMAIL_SMTP)
                server.login(EMAIL_SENDER, EMAIL_PWD)
                server.sendmail(EMAIL_SENDER, _receivers, msg.as_string())
                self.logger.info("发送邮件成功")
            except SMTPException as e:
                self.logger.error(e)
        else:
            self.logger.info("本次没有news")

    def send_live_email(self, _articles=None):
        if _articles and len(_articles) > 0:
            _receivers = ','.join(EMAIL_RECEIVERS)
            # print(_receivers)
            html_msg = self.build_up_live_html(_articles)
            # print(html_msg)

            jsonobj = get_price("BTCUSDT")
            btc_price = jsonobj['price']

            msg = MIMEText(html_msg, 'html', 'utf-8')
            msg['From'] = _format_addr('共 %d 条新快讯，敬请查看 <%s>' % (len(_articles), EMAIL_SENDER))
            msg['To'] = _format_addr('收件人 <%s>' % _receivers[0])
            msg['Subject'] = "币安BTC当前报价:%s" % btc_price
            try:
                server = smtplib.SMTP(EMAIL_SMTP)
                server.login(EMAIL_SENDER, EMAIL_PWD)
                server.sendmail(EMAIL_SENDER, _receivers, msg.as_string())
                self.logger.info("发送邮件成功")
            except SMTPException as e:
                self.logger.error(e)
        else:
            self.logger.info("本次没有live消息")

    def build_up_html(self, _articles):
        content = []
        for article in _articles:
            _str = self.news_template % (article['url'], article['title'], article['remark'], article['desc'])
            content.append(_str)

        return self.html_template % (''.join(content))

    def build_up_live_html(self, _articles):
        content = []
        for article in _articles:
            if 'desc' in article:
                _str = self.live_template % (article['desc'])
                content.append(_str)

        return self.html_template % (''.join(content))
