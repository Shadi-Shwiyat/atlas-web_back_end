#!/usr/bin/env python3
'''Simple redis caching system'''
import redis
import uuid
from typing import Union


class Cache():
    '''Simple cache system using
    redis'''
    def __init__(self) -> None:
        '''Create private instance
        of redis client and flush it'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union(str,
                                bytes,
                                int,
                                float)) -> str:
        '''Returns stringified version
        of the passed in data, stores data
        using random key from uuid()'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
