#!/usr/bin/env python3
"""class LIFOCache inheriting BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching system"""

    def __init__(self):
        """initializing LIFO cache"""
        super().__init__()

    def put(self, key, item):
        """Add item in cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key) if key is not None else None
