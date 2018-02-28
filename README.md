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


## ChangLog

2.23 微信机器人定义
2.23 新增对zb & coinmarkket 等平台的coin报价
2.23 修改wechat robot 回复随机延时机制，模拟人类
2.24 项目重构，同时支持python3 以及 python2
2.24 增加对okex、binance、huobi交易所的货币币价查询
2.24 定义查询币价的通用格式
2.25 新增爬虫: 财新网(caixin)、一财网(yicai)
2.26 新增爬虫: 华尔街见闻(wallstreetcn)、华尔街见闻快讯(wallstreetcn_live)
2.26 增加缓存机制：所有查询币价的api 增加缓存cache机制
2.26 新闻和快讯爬虫 增加关键词过滤（区块链等关键词)
2.26 增加定时启动机制 服务
2.27 增加smtp邮件推送服务
2.27 增加coin 挂单深度查询
2.27 新增 全球加密货币总市值查询
2.28 修复服务器端25端口被禁用导致邮件无法推动的异常

