from config import FILTER_KEYWORDS
from service_redis_cache import RedisCache

db = RedisCache('spider_cursor')


def filter_news(spider_key, _article=None):
    """
    # 1. _cursor > history_index
    # 2. desc 含 关键词
    :param spider_key: 
    :param _article: 
    :return: 
    """
    if _article and ('title' in _article) and ('desc' in _article) and ('_cursor' in _article):
        _cursor = int(_article['_cursor'])
        _history_index = db.get(spider_key)
        if _history_index is None:
            _history_index = -1
        # print('%d , %d ' % (_cursor, _history_index))
        if (not _history_index) or (_history_index and _cursor > _history_index):
            _desc = _article['desc']
            if any(str_ in _desc for str_ in FILTER_KEYWORDS):
                return True
    return False


def filter_live(spider_key, _article=None):
    """
    # 1. _cursor > history_index
    # 2. desc 含 关键词
    :param spider_key: 
    :param _article: 
    :return: 
    """
    if _article and ('desc' in _article) and ('_cursor' in _article):
        _cursor = int(_article['_cursor'])
        _history_index = db.get(spider_key)

        if _history_index is None:
            _history_index = -1
        # print('%d , %d ' % (_cursor, _history_index))
        if _cursor > _history_index:
            return True
    return False


def save_cursor(key, value):
    db.set(key=key, value=value)
