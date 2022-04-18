import pytest

from heaps.heap import Heap


class TestHeap:
    @pytest.fixture(autouse=True)
    def init_test_heap(self):
        self.heap = Heap([1, 5, 7, 3, 6, 4])

    def test_heap(self):
        assert self.heap.numbers == []
