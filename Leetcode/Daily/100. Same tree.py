from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def root(i, j):
            if i and j and i.val == j.val:
                left = root(i.left, j.left)
                right = root(i.right, j.right)
                return left and right
            if i == j is None:
                return True
            return False

        return root(p, q)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(3)
print(Solution().isSameTree(p, q))
