from config import FILTER_KEYWORDS

def filter_article(spider_key, _article=None):
    """
    # 1. _cursor > history_index
    # 2. desc 含 关键词
    :param _article: 
    :return: 
    """
    if _article and ('title' in _article) and ('desc' in _article) and ('_cursor' in _article):
        _cursor = int(_article['_cursor'])
        _history_index = 1
        if _cursor > _history_index:
            _desc = _article['_cursor']
            if any(str_ in _desc for str_ in FILTER_KEYWORDS):
                return True
    return False


def save_cursor(key,value):
    cache = None