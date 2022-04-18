from dataclasses import dataclass
from typing import List


@dataclass
class Heap:

    numbers: List[int]

    def __post_init__(self) -> None:
        self._heapify()  # turns given list into heap

    def _heapify(self) -> None:
        """Heapify a given array of numbers."""
        pass

    def insert(self, num: int) -> None:
        """Insert number into heap.

        Args:
            num (int): The number to insert into the heap.
        """
        pass

    def pop(self) -> int:
        """Pop the min/max number from the heap.

        Returns:
            int: The min/max number from the heap.
        """
        pass

    def peek(self) -> int:
        """Peek the min/max number from the heap.

        Returns:
            int: The min/max number from the heap.
        """
        pass

    def size(self) -> int:
        """Get the current size of the heap.

        Returns:
            int: The size of the heap.
        """
        pass
