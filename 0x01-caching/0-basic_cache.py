#!/usr/bin/env python3
"""class BasicCache inheriting BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching withouy size limit"""

    def put(self, key, item):
        """Add item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item for cache"""
        return self.cache_data.get(key) if key is not None else None
