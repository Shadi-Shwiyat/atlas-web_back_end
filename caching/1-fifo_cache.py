#!/usr/bin/env python3
'''Script creates a caching system
    using inheritance from BaseCaching
    and follows a FIFO cache replacement
    policy'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Class inherits from BaseCaching to
        modify its put and get methods. Uses a FIFO
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
            # Use list method to get the first key/value pair
            # by insertion order
            first_key, first_value = list(self.cache_data.items())[0]
            # print(first_key)
            del self.cache_data[first_key]
            self.cache_data[key] = item
            print(f'DISCARD:', first_key)
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
