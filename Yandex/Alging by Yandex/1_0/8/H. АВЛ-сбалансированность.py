class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeSearch:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, node: BinaryTreeNode):
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while curr:
                if curr.val == node.val:
                    return
                if curr.val < node.val:
                    if curr.right is None:
                        curr.right = node
                        return
                    else:
                        curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = node
                        return
                    else:
                        curr = curr.left

    def check_balance(self, root: BinaryTreeNode):
        if root is None:
            return 0
        left = self.check_balance(root.left)
        right = self.check_balance(root.right)
        if left is not None and right is not None:
            if abs(left - right) <= 1:
                return max(left, right) + 1




tree = BinaryTreeSearch()
ans = []
for val in tuple(map(int, input().split()))[:-1]:
    node = BinaryTreeNode(val)
    tree.add_node(node)
print('NO' if tree.check_balance(tree.root) is None else 'YES')
