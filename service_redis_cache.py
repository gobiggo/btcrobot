#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import pickle
from functools import wraps

from redis import Redis
from redis import ConnectionPool
from config import REDIS_DB
from config import REDIS_HOST
from config import REDIS_PORT

import logging


logger = logging.getLogger(__name__)


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


# @singleton()
class RedisCache(object):
    MAX_EXPIRES = 86400
    SERIALIZER = pickle
    LOCKER = set()

    def __init__(self, name, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, max_expires=MAX_EXPIRES):
        self.name = name
        self.max_expires = max_expires
        # self.redis_pool = ConnectionPool(host=host, port=port, db=db, decode_responses=True)
        # self.db = Redis(connection_pool=self.redis_pool)
        self.db = Redis(host=host, port=port, db=db)

    def _getkey(self, *keys):
        return ":".join([self.name] + list(keys))

    def _get_data(self, key):
        result = self.db.get(key)
        return None if result == b'None' else result

    def get(self, key):
        result = self._get_data(self._getkey(key))
        return self.SERIALIZER.loads(result) if result is not None else result

    def set(self, key, value, ex=None):
        k = self._getkey(key)
        v = self.SERIALIZER.dumps(value)
        if ex is None:
            self.db.set(k, v)
        else:
            self.db.setex(k, v, ex)

    def delete(self, key):
        self.db.delete(self._getkey(key))

    @staticmethod
    def build_key(name, *args, **kwargs):
        m = hashlib.md5()
        m.update(name.encode('utf-8'))
        m.update(pickle.dumps(args))
        m.update(pickle.dumps(kwargs))
        return m.hexdigest()

    def cached(self, key, func, ex=None):
        if ex is None:
            ex = self.max_expires
        min_ttl = self.max_expires - ex  # ex <= 0 : force refresh data
        key = "#".join([self.name, key])
        result = self._get_data(key)
        if key not in self.LOCKER:
            self.LOCKER.add(key)
            try:
                ttl = self.db.ttl(key)
                if ttl is None or ttl < min_ttl:
                    result = func()
                    if result is not None:
                        result = self.SERIALIZER.dumps(result)
                    self.db.setex(key, result, self.max_expires)
            finally:
                self.LOCKER.remove(key)
        try:
            result = self.SERIALIZER.loads(result) if result is not None else None
        except:
            pass
        return result


def redis_cached(db, ex=None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            key = RedisCache.build_key(fn.__name__, *args, **kwargs)
            return db.cached(key, lambda: fn(*args, **kwargs), ex)
        return wrapper
    return decorator
