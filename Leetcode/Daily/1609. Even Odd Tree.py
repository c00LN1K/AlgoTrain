# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        last_odd = 0
        last_odd_level = 0
        last_even = math.inf
        last_even_level = 1
        d.append([root, 0])
        while d:
            root, level = d.popleft()
            if level % 2 != root.val % 2:
                return False
            if level % 2 == 0:
                if level >= last_odd_level and last_odd < root.val or level > last_odd_level:
                    if level > last_odd_level:
                        last_odd_level = level
                    last_odd = root.val
                    if root.left:
                        d.append([root.left, level + 1])
                    if root.right:
                        d.append([root.right, level + 1])
                else:
                    return False
            else:
                if level == last_even_level and last_even > root.val or level > last_even_level:
                    if level > last_even_level:
                        last_even_level = level
                    last_even = root.val
                    if root.left:
                        d.append([root.left, level + 1])
                    if root.right:
                        d.append([root.right, level + 1])
                else:
                    return False
        return True


root = TreeNode(1)

b1 = TreeNode(10)
b2 = TreeNode(4)

b3 = TreeNode(3)
b4 = TreeNode(7)
b5 = TreeNode(9)

b6 = TreeNode(12)
b7 = TreeNode(8)
b8 = TreeNode(6)
b9 = TreeNode(2)

root.left = b1
b1.left = b3
b3.left = b6
b3.right = b7

root.right = b2
b2.left = b4
b2.right = b5
b4.left = b8
b5.right = b9
print(Solution().isEvenOddTree(root))
