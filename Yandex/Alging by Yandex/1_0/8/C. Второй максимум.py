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

    def get_second_maximum(self):
        prev, curr = None, self.root
        while curr.right:
            prev, curr = curr, curr.right
        if curr.left is None:
            return prev.val
        curr = curr.left
        while curr.right:
            curr = curr.right
        if prev is None:
            return curr.val
        return max(curr.val, prev.val)





tree = BinaryTreeSearch()
ans = []
for val in tuple(map(int, input().split()))[:-1]:
    node = BinaryTreeNode(val)
    tree.add_node(node)

print(tree.get_second_maximum())