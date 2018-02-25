## 安装python3

    https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz

    xz -d 
    tar -xvf
    
    ./configure --prefix=/usr/local/python3 --with-ssl --enable-loadable-sqlite-extensions && make && sudo make install
    
    
    rm -rf /usr/bin/python3
    rm -rf /usr/bin/pip3
    
    ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
    ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3


## 安装依赖

    # redis 操作 https://www.jianshu.com/p/2639549bedc8
    pip install redis
    
    pip install coinbase
    
    pip install wxpy
    
## 爬虫依赖

    # 安装 BeautifulSoup & lxml
    
    pip install beautifulsoup4
    pip install html5lib
    pip install lxml
    
    