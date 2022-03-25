from symmetric_tree.main import TreeNode, is_symmetric_iterative, is_symmetric_recursive


def build_tree(
    node_values: list,
    root: TreeNode,
    index: int,
) -> TreeNode:
    """Build binary tree from given list.

    Args:
        node_values (list): The list of node values
        root (TreeNode): The root of the binary tree
        index (int): The current index of the list

    Returns:
        TreeNode: The root TreeNode of the binary tree
    """
    if index < len(node_values):
        root = TreeNode(node_values[index])
        root.left = build_tree(node_values, root.left, 2 * index + 1)
        root.right = build_tree(node_values, root.right, 2 * index + 2)
    return root


class TestSymmetricTree:
    def test_single_node_tree(self):
        root = None
        root = build_tree([1], root, 0)
        assert is_symmetric_iterative(root) is True
        assert is_symmetric_recursive(root) is True

    def test_simple_unbalanced_tree(self):
        root = None
        root = build_tree([1, 2], root, 0)
        assert is_symmetric_iterative(root) is False
        assert is_symmetric_recursive(root) is False

    def test_simple_symmetrical_tree(self):
        root = None
        root = build_tree([1, 2, 2], root, 0)
        assert is_symmetric_recursive(root) is True
        assert is_symmetric_iterative(root) is True

    def test_simple_balanced_nonsymmetrical_tree(self):
        root = None
        root = build_tree([1, 2, 3], root, 0)
        assert is_symmetric_recursive(root) is False
        assert is_symmetric_iterative(root) is False

    def test_unbalanced_tree(self):
        root = None
        root = build_tree([1, 2, 2, 3], root, 0)
        assert is_symmetric_recursive(root) is False
        assert is_symmetric_iterative(root) is False

    def test_complex_symmetrical_tree(self):
        root = None
        root = build_tree([1, 2, 2, 3, 4, 4, 3, 7, 8, 4, 2, 2, 4, 8, 7], root, 0)
        assert is_symmetric_recursive(root) is True
        assert is_symmetric_iterative(root) is True
