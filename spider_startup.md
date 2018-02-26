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
  

0,2 6-24 * * * * /usr/bin/python /data/btc_robot/robot_spider_live.py
0,10 6-24 * * * /usr/bin/python /data/btc_robot/robot_spider.py