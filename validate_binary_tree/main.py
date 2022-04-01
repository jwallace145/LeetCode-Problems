from typing import Optional

# CONSTRAINTS
MIN_VALUE = -2 ^ 31
MAX_VALUE = 2 ^ 31 - 1


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst_helper(
    root: Optional[TreeNode], min_bound: int, max_bound: int
) -> bool:
    if root is None:
        return True

    if (root.val and root.val <= min_bound) or (root.val and root.val >= max_bound):
        return False

    return is_valid_bst_helper(root.left, min_bound, root.val) and is_valid_bst_helper(
        root.right, root.val, max_bound
    )


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Verify if the given tree is a valid BST or not.

    Args:
        root (Optional[TreeNode]): The root of the BST.
    """
    # if its an empty tree return true
    return is_valid_bst_helper(root, min_bound=MIN_VALUE, max_bound=MAX_VALUE)
