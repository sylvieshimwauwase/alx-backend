#!/usr/bin/env python3
"""class FIFOCache inheriting BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """initializing FIFO cache"""
        super().__init__()

    def put(self, key, item):
        """Add item in cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key) if key is not None else None
