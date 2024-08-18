from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if root.left is None and root.right is None:
                up = root.val - 1
                self.ans += abs(up)
                return up

            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0

            up = left + right + root.val - 1
            self.ans += abs(up)
            return up

        dfs(root)
        return self.ans


root = TreeNode(3, TreeNode(), TreeNode())

print(Solution().distributeCoins(root))
