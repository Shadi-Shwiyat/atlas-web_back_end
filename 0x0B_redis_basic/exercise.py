#!/usr/bin/env python3
'''Simple redis caching system'''
import redis
import uuid
from typing import Union, Callable


class Cache():
    '''Simple cache system using
    redis'''
    def __init__(self) -> None:
        '''Create private instance
        of redis client and flush it'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str,
                                bytes,
                                int,
                                float]) -> str:
        '''Returns stringified version
        of the passed in data, stores data
        using random key from uuid()'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable=None) -> bytes:
        '''Gets data from db and returns as
        byte string'''
        if fn:
            value = self._redis.get(key)
            if not value:
                return None

            formatted_value = fn(value)
            return formatted_value
        else:
            value = self._redis.get(key)
            if not value:
                return None

            return value

    def get_str(self, value: bytes) -> str:
        '''Returns bytes string converted
        to regular string'''
        decoded_string = value.decode('utf-8')
        return decoded_string

    def get_int(self, value: bytes) -> int:
        '''Returns bytes converted to int'''
        decoded_int = int(value)
        return decoded_int
