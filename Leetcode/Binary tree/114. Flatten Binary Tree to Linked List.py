# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root
        """
        Do not return anything, modify root in-place instead.
        """
        self.actual = root

        def make_linked_list(root):
            if root is None:
                return None
            self.actual.right = root
            self.actual.left = None
            self.actual = root
            make_linked_list(root.left)
            make_linked_list(root.right)
        make_linked_list(root.left)
        return ''


root = TreeNode(1)
left1, right1 = TreeNode(2), TreeNode(5)
left2, right2 = TreeNode(3), TreeNode(4)
right3 = TreeNode(6)

root.left, root.right = left1, right1
left1.left, left1.right = left2, right2
right1.right = right3

print(Solution().flatten(root))
