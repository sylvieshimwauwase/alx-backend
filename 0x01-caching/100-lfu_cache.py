#!/usr/bin/env python3
"""class LFUCache inheriting BaseCaching"""
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """LFU caching system."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency_counter = {}

    def put(self, key, item):
        """Assign an item to the cache using LFU algorithm."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:

                min_frequency = min(self.frequency_counter.values())
                keys_with_min_frequency = [k for k, v in self.frequency_counter.items() if v == min_frequency]

                if len(keys_with_min_frequency) == 1:
                    discarded_key = keys_with_min_frequency[0]
                else:
                    discarded_key = min(self.cache_data, key=lambda k: self.cache_data[k])

                del self.cache_data[discarded_key]
                del self.frequency_counter[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.frequency_counter[key] = 1

    def get(self, key):
        """Retrieve the value linked to the key from the cache."""
        if key is not None and key in self.cache_data:
            self.frequency_counter[key] += 1
            return self.cache_data[key]
        else:
            return None
