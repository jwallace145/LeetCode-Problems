from lru_cache.main import LRUCache
import pytest


class TestLRUCache:
    @pytest.fixture(autouse=True)
    def init_test_lru_cache(self):
        self.lru_cache = LRUCache(capacity=2)

    def test_eviction_policy(self):
        self.lru_cache.set(1, 1)
        self.lru_cache.set(2, 2)
        self.lru_cache.set(3, 3)
        assert 1 not in self.lru_cache.cache
        assert 2 in self.lru_cache.cache
        assert 3 in self.lru_cache.cache
        assert self.lru_cache.get(2) == 2
        assert self.lru_cache.get(3) == 3
        assert self.lru_cache.get(1) == -1
