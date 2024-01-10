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
        self.last_inserted_key = None

    def put(self, key, item):
        '''assigns to cache_data dictionary item value
            for each corresponding key, if key or item is
            None, method does nothing, track the last item
            that was added to dictionary using variable'''
        if key is None or item is None:
            return None
        elif (len(self.cache_data) is BaseCaching.MAX_ITEMS
              and key not in self.cache_data):
            # Use variable to get last inserted value
            # and delete it
            print(f'DISCARD:', self.last_inserted_key)
            self.cache_data[key] = item
            del(self.cache_data[self.last_inserted_key])
            self.last_inserted_key = key
        else:
            self.cache_data[key] = item
            self.last_inserted_key = key

    def get(self, key):
        '''returns value in cache_data dictionary linked
            to passed in key'''
        if key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            return value
