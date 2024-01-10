#!/usr/bin/env python3
'''Script creates a caching system
    using inheritance from BaseCaching
    and follows a LRU cache replacement
    policy'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Class inherits from BaseCaching to
        modify its put and get methods. Uses a LRU
        caching replacement policy'''
    def __init__(self):
        '''Call init method of parent class for access to
            cache_data dictionary'''
        super().__init__()
        self.most_recent = []

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
            least_used = self.most_recent[0]
            print(f'DISCARD:', least_used)
            del self.cache_data[least_used]
            self.cache_data[key] = item
            self.lru_maintainer(key)
        else:
            self.lru_maintainer(key)
            self.cache_data[key] = item

    def lru_maintainer(self, key):
        '''function keeps track of the most recent item
            used and pushes it to the top of the list
            so that least used item can be deleted'''
        if (len(self.most_recent) is BaseCaching.MAX_ITEMS
                and key in self.most_recent):
            # print(self.most_recent)
            self.most_recent.remove(key)
            self.most_recent.append(key)
            # print(self.most_recent)
        elif (len(self.most_recent) is BaseCaching.MAX_ITEMS
              and key not in self.most_recent):
            # print(self.most_recent)
            self.most_recent.remove(self.most_recent[0])
            self.most_recent.append(key)
            # print(self.most_recent)
        else:
            # print(self.most_recent)
            self.most_recent.append(key)
            # print(self.most_recent)

    def get(self, key):
        '''returns value in cache_data dictionary linked
            to passed in key'''
        if key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            return value
