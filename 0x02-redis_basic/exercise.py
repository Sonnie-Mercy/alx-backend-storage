#!/usr/bin/env python3
"""
instance of the redis client
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """call_history decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{self.__class__.__qualname__}.{method.__name__}"
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper

def count_calls(method: Callable) -> Callable:
    """count calls decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{self.__class__.__qualname__}.{method.__name__}"
        count_key = f"{key}:count"
        count = self._redis.incr(count_key)
        return method(self, *args, **kwargs)
    return wrapper

def replay(method: Callable) -> None:
    """replay method"""
    key = f"{method.__qualname__}:inputs"
    inputs = cache._redis.lrange(key, 0, -1)

    key = f"{method.__qualname__}:outputs"
    outputs = cache._redis.lrange(key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8').strip()},) -> {output.decode('utf-8')}")

class Cache:
    """
    The cache class
    """
    def __init__(self):
        """initial method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, None]:
        """get method"""
        data = self._redis.get(key)

        if data is not None:
            if fn is not None:
                return fn(data)
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """get_str method"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """get_int method"""
        return self.get(key, fn=int)
