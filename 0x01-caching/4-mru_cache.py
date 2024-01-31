#!/usr/bin/python3
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """Most Recently Used (MRU) caching system."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()

    def put(self, key, item):
        """Assign an item to the cache using MRU algorithm."""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = max(self.cache_data, key=lambda k: self.cache_data[k])
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
                
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value linked to the key from the cache."""
        return self.cache_data.get(key) if key is not None else None
