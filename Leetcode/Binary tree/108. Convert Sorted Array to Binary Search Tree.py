# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def make_tree(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = make_tree(start, mid - 1)
            root.right = make_tree(mid + 1, end)
            return root
        return make_tree(0, len(nums) - 1)


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
