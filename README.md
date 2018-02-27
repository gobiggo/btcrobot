### vultr 不能发邮件

    本地可以发送邮件，但是通过vultr 服务器怎么也发不出了，总是报连接超时
    telnet smtp.163.com 25

### 安装python3

    https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz

    xz -d 
    tar -xvf
    
    ./configure --prefix=/usr/local/python3 --with-ssl --enable-loadable-sqlite-extensions && make && sudo make install
    
    
    rm -rf /usr/bin/python3
    rm -rf /usr/bin/pip3
    
    ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
    ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3


### 安装依赖

    # redis 操作 https://www.jianshu.com/p/2639549bedc8
    pip install redis
    
    /usr/local/bin/redis-server /etc/redis.conf
    keys * 
    flushdb
    
    pip install coinbase
    
    pip install wxpy
    
    pip install numpy
    
### 爬虫依赖

    # 安装 BeautifulSoup & lxml
    
    pip install beautifulsoup4
    pip install html5lib
    pip install lxml
    
## to-do list

- cmc symbol_bitid 抓取
- wxpy 拦截注册（是否可以动态给群加register
- 配置文件动态更新（通过文件助手、我个人微信)
- tools 方法重构
- 增加coin 挂单深度查询

## ChangLog

2.23 wechat robot
2.23 zb & coinmarkket coin报价
2.23 wechat robot 模拟人类，增加一定随机延时
2.24 转换为python3 以及 项目重构
2.24 增加okex、binance、huobi的coin price
2.24 定义查询币价的通用格式
2.25 增加spider: caixin、wallstreetcn、wallstreetcn_live 
2.26 增加spider: yicai
2.26 查询币价的api 增加缓存cache
2.26 spider 增加关键词过滤
2.26 增加定时crontab 服务