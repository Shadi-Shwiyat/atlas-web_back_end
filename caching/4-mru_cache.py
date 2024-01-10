#!/usr/bin/env python3
'''Script creates a caching system
    using inheritance from BaseCaching
    and follows a MRU cache replacement
    policy'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Class inherits from BaseCaching to
        modify its put and get methods. Uses a MRU
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
            most_used = self.most_recent[-1]
            print(f'DISCARD:', most_used)
            del self.cache_data[most_used]
            self.cache_data[key] = item
            self.mru_maintainer(key)
        else:
            self.mru_maintainer(key)
            self.cache_data[key] = item

    def mru_maintainer(self, key):
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
            self.mru_maintainer(key)
            value = self.cache_data[key]
            return value
