import redis
import pickle
import functools
from logger import Logger


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class RedisService:
    def __init__(self):
        self.logging = Logger().get_log()
        self.logging.info("init RedisService")
        self.default_ex_time = 60
        self.enable = True
        self.redis_pool = redis.ConnectionPool(host='10.10.1.252', port=6379, decode_responses=True)

    def read(self, key):
        if self.enable:
            r = redis.Redis(connection_pool=self.redis_pool)
            val = r.get(key)
            if val is None:
                return None
            else:
                self.logging.info("===get val from redis;key=%s", key)
                return pickle.loads(val)
        else:
            # print "disable cache"
            return None

    def write(self, key, val, ex=None):
        r = redis.Redis(connection_pool=self.redis_pool)
        if val is None:
            self.logging.info("===Write Failed : the val is None")
        else:
            if ex and ex > 0:
                _ex = ex
            else:
                _ex = self.default_ex_time
            r.set(key, pickle.dumps(val), ex=_ex)
            self.logging.info("===write val to redis;key=%s", key)

    def enable(self, _enable=True):
        self.enable = _enable


def cache(f, ex=None):
    def wrapper(*args, **kwargs):
        #print f.__name__
        key = pickle.dumps((f.__name__, args, kwargs)).replace("\n", "")
        #print "=== key :%s" % key
        rs = RedisService()
        val = rs.read(key)
        if val is None:
            val = f(*args, **kwargs)  # call the wrapped function, save in cache
            rs.write(key, val, ex)
        return val  # read value from cache

    functools.update_wrapper(wrapper, f)  # update wrapper's metadata
    return wrapper
