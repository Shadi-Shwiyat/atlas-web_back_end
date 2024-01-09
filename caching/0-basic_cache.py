#!/usr/bin/env python3
'''Script creates a basic caching system
    using inheritance from BaseCaching'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Class inherits from BaseCaching to
        modify its put and get methods'''
    def __init__(self):
        '''Call init method of parent class for access to
            cache_data dictionary'''
        super().__init__()

    def put(self, key, item):
        '''assigns to cache_data dictionary item value
            for each corresponding key, if key or item is
            None, method does nothing'''
        if key is None or item is None:
            return None
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''returns value in cache_data dictionary linked
            to passed in key'''
        if key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            return value
