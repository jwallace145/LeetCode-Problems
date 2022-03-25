from typing import Optional


class TreeNode:
    """Binary Tree Node

    A binary tree is a tree data structure in which each node has at most two children.
    """

    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val  # node value
        self.left = left  # pointer to left child, could be None
        self.right = right  # pointer to right child, could be None


def symmetric_check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    # if left and right nodes do not exist, return True
    if not left and not right:
        return True

    # if left or right nodes do not exist (XOR) => unbalanced tree, return False
    if not left or not right:
        return False

    # at this point, we know both children nodes exist, commpare their values
    # if values are equal, continue to recurse and ensure child trees are
    # symmetric as well
    if left.val == right.val:
        return symmetric_check(left.right, right.left) and symmetric_check(
            left.left, right.right
        )

    # if the left and right values do not equal each other, return False
    return False


def is_symmetric_recursive(root: Optional[TreeNode]) -> bool:
    """Checks to see if given binary tree is a symmetrical tree or not recursively.

    Args:
        root (Optional[TreeNode]): The root node of the given binary tree

    Returns:
        (bool): The boolean value of if the binary tree is symmetrical or not
    """
    # ensure the left and right subtrees are symmetrical => binary tree is symmetrical
    return symmetric_check(root.left, root.right)


def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
    """Checks to see if given binary tree is a symmetrical tree or not iteratively.

    Args:
        root (Optional[TreeNode]): The root node of the given binary tree

    Returns:
        (bool): The boolean value of if the binary tree is symmetrical or not
    """
    if not root:
        return True

    # recursive approach implies stack approach to iterating through binary tree
    stack = [[root.left, root.right]]

    while len(stack):
        pair = stack.pop(0)
        left = pair[0]
        right = pair[1]

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val == right.val:
            stack.insert(0, [left.left, right.right])
            stack.insert(0, [left.right, right.left])
        else:
            return False

    return True
