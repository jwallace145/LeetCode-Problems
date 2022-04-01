from validate_binary_tree.main import TreeNode, is_valid_bst


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


class TestValidTree:
    def test_empty_tree(self):
        root = None
        assert is_valid_bst(root) == True

    def test_simple_tree(self):
        root = None
        root = build_tree([2, 1, 3], root, 0)
        assert is_valid_bst(root) == True

    def test_simple_false(self):
        root = None
        root = build_tree([5, 1, 4, None, None, 3, 6], root, 0)
        assert is_valid_bst(root) == False
