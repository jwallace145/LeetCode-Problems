from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Node:
    """Doubly Linked List Node"""

    key: int
    value: int
    previous: Any = None  # pointer to previous node
    next: Any = None  # pointer to next node


@dataclass
class LRUCache:
    """Least Recently Used Cache"""

    capacity: int
    cache: Dict[int, Node] = field(default_factory=lambda: {})
    head: Node = Node(0, 0)
    tail: Node = Node(0, 0)

    def __post_init__(self) -> None:
        # initialize doubly linked list
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # get node from cache dictionary, constant retrieval time
            node = self.cache.get(key)

            # remove node from doubly linked list and add to front to represent new order
            self._remove_node(node)
            self._add_node(node)

            return node.value
        return -1

    def set(self, key: int, value: int) -> int:
        # if key is in cache, remove it so we can update precendence
        if key in self.cache:
            self._remove_node(self.cache.get(key))
        # update precedence
        node = Node(key, value)
        self._add_node(node)
        self.cache[key] = node

        # if the size of the cache is greater than capacity, we have to evict something
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove_node(node)
            del self.cache[node.key]

    def _remove_node(self, node: Node) -> None:
        previous_node = node.previous
        next_node = node.next
        previous_node.next = next_node
        next_node.previous = previous_node

    def _add_node(self, node: Node) -> None:
        previous_node = self.tail.previous
        previous_node.next = node
        node.previous = previous_node
        self.tail.previous = node
        node.next = self.tail
