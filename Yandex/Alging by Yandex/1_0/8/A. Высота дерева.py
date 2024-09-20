class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeSearch:
    def __init__(self, root=None):
        self.root = root
        self.maxDepth = 0

    def addNode(self, node: BinaryTreeNode):
        curr_depth = 0
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while curr:
                curr_depth += 1
                if curr.val == node.val:
                    curr_depth -= 1
                    break
                elif curr.val < node.val:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
        self.maxDepth = max(self.maxDepth, curr_depth + 1)

tree = BinaryTreeSearch()
for val in tuple(map(int, input().split()))[:-1]:
    node = BinaryTreeNode(val)
    tree.addNode(node)

print(tree.maxDepth)