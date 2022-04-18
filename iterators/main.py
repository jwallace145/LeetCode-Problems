from dataclasses import dataclass, field
from typing import Any

from iterators.exceptions import BSTIndexOutOfRange


@dataclass
class BSTNode:

    value: int
    right: Any = None
    left: Any = None


@dataclass
class BSTIterator:

    root: BSTNode
    _inorder: list = field(default_factory=lambda: [])
    _inorder_index: int = 0
    _preorder: list = field(default_factory=lambda: [])
    _preorder_index: int = 0
    _postorder: list = field(default_factory=lambda: [])
    _postorder_index: int = 0

    def __post_init__(self) -> None:
        self.traverse_inorder(self.root)
        self.traverse_preorder(self.root)
        self.traverse_postorder(self.root)

    def traverse_inorder(self, root: BSTNode) -> None:
        if root:
            self.traverse_inorder(root.left)
            self._inorder.append(root)
            self.traverse_inorder(root.right)

    def traverse_preorder(self, root: BSTNode) -> None:
        if root:
            self._preorder.append(root)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self, root: BSTNode) -> None:
        if root:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            self._postorder.append(root)

    def inorder_next(self) -> BSTNode:
        if self._inorder_index in range(len(self._inorder)):
            next_node = self._inorder[self._inorder_index]
            self._inorder_index += 1
            return next_node
        raise BSTIndexOutOfRange()

    def preorder_next(self) -> BSTNode:
        if self._preorder_index in range(len(self._preorder)):
            next_node = self._preorder[self._preorder_index]
            self._preorder_index += 1
            return next_node
        raise BSTIndexOutOfRange()

    def postorder_next(self) -> BSTNode:
        if self._postorder_index in range(len(self._postorder)):
            next_node = self._postorder[self._postorder_index]
            self._postorder_index += 1
            return next_node
        raise BSTIndexOutOfRange()
