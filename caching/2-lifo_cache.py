#!/usr/bin/env python3
'''Script creates a caching system
    using inheritance from BaseCaching
    and follows a LIFO cache replacement
    policy'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Class inherits from BaseCaching to
        modify its put and get methods. Uses a LIFO
        caching replacement policy'''
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
        elif len(self.cache_data) is BaseCaching.MAX_ITEMS:
            # print(len(self.cache_data))
            # Use list method to get the last key/value pair
            # by insertion order
            last_key, last_value = list(self.cache_data.items())[BaseCaching.MAX_ITEMS - 1]
            print(list(self.cache_data.items())[BaseCaching.MAX_ITEMS - 1])
            del self.cache_data[last_key]
            self.cache_data[key] = item
            print(f'DISCARD:', last_key)
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
