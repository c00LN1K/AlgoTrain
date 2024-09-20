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

    def get_order(self, lst, root=None):
        if root is None:
            root = self.root
        if root.left:
            self.get_order(lst, root.left)
        lst.append(root.val)
        if root.right:
            self.get_order(lst, root.right)

tree = BinaryTreeSearch()
ans = []
for val in tuple(map(int, input().split()))[:-1]:
    node = BinaryTreeNode(val)
    tree.add_node(node)

tree.get_order(ans)
print(*ans)
