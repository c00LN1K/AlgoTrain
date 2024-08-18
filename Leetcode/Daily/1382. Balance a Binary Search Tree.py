# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def count(root):
            if not root:
                return 0
            d = deque()
            d.append(root)
            k = 0
            while d:
                k += 1
                for i in range(len(d)):
                    node = d.popleft()
                    if node.left: d.append(node.left)
                    if node.right: d.append(node.right)
            return k

        delta = count(root.left) - count(root.right)
        if abs(delta) <= 1:
            return root

        self.new_root = None

        def dfs(root, delta):
            if delta:
                if root.left:
                    node = dfs(root.left, delta - 1)
                    node.right = root
                    root.left = None
                else:
                    node = dfs(root.right, delta - 1)
                    node.left = root
                    root.right = None
            else:
                self.new_root = root
            return root

        dfs((root.left if delta > 0 else root.right), abs(delta) - 2)
        if delta > 0:
            root.left.right, root.left = root, None
        else:
            root.right.left, root.right = root, None
        return self.new_root


root = TreeNode(19)
root.left = TreeNode(10)
root.left.left = TreeNode(4)
root.left.right = TreeNode(17)
root.left.left.right = TreeNode(5)


root = Solution().balanceBST(root)


def dfs(root):
    if root is None: print('None'); return
    print(root)
    dfs(root.left)
    dfs(root.right)


dfs(root)
