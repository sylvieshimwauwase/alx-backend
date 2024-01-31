#!/usr/bin/env python3
"""class LFUCache inheriting BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """(LRU caching system."""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """Assign an item to the cache using LRU algorithm."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order_used.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """Retrieve the value linked to the key from the cache."""
        if key is not None and key in self.cache_data:
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        else:
            return None
