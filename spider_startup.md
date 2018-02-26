## crontab

https://my.oschina.net/rotiwen/blog/89711

```
    service crond start //启动服务
    service crond stop //关闭服务
    service crond restart //重启服务
    service crond reload //重新载入配置
```

crontab命令

```
  -e 　编辑该用户的计时器设置。 
　-l 　列出该用户的计时器设置。 
　-r 　删除该用户的计时器设置。
```
  

0,2 6-22 * * * * /usr/bin/python /data/btc_robot/mail_live_spider.py
0,10 6-20 * * * /usr/bin/python /data/btc_robot/mail_news_spider.py