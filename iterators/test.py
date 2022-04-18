import pytest

from iterators.main import BSTIterator, BSTNode


def build_tree(
    node_values: list,
    root: BSTNode,
    index: int,
) -> BSTNode:
    """Build binary tree from given list.

    Args:
        node_values (list): The list of node values
        root (TreeNode): The root of the binary tree
        index (int): The current index of the list

    Returns:
        TreeNode: The root TreeNode of the binary tree
    """
    if index < len(node_values):
        root = BSTNode(node_values[index])
        root.left = build_tree(node_values, root.left, 2 * index + 1)
        root.right = build_tree(node_values, root.right, 2 * index + 2)
    return root


class TestBSTIterator:
    @pytest.fixture(autouse=True)
    def init_test_bst_iterator(self):
        root = build_tree([1, 2, 3, 4, 5], None, 0)
        self.bst_iterator = BSTIterator(root)

    def test_bst_iterator_inorder_simple(self):
        assert self.bst_iterator.inorder_next().value == 4
        assert self.bst_iterator.inorder_next().value == 2
        assert self.bst_iterator.inorder_next().value == 5
        assert self.bst_iterator.inorder_next().value == 1
        assert self.bst_iterator.inorder_next().value == 3

    def test_bst_iterator_preorder_simple(self):
        assert self.bst_iterator.preorder_next().value == 1
        assert self.bst_iterator.preorder_next().value == 2
        assert self.bst_iterator.preorder_next().value == 4
        assert self.bst_iterator.preorder_next().value == 5
        assert self.bst_iterator.preorder_next().value == 3

    def test_bst_iterator_postorder_simple(self):
        assert self.bst_iterator.postorder_next().value == 4
        assert self.bst_iterator.postorder_next().value == 5
        assert self.bst_iterator.postorder_next().value == 2
        assert self.bst_iterator.postorder_next().value == 3
        assert self.bst_iterator.postorder_next().value == 1
