class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, num):
        if self.root is None:
            self.root = TreeNode(num)
            return 'DONE'
        curr = self.root
        while curr:
            if curr.val == num:
                return 'ALREADY'
            if curr.val < num:
                if curr.right is None:
                    curr.right = TreeNode(num)
                    return 'DONE'
                curr = curr.right
            elif curr.val > num:
                if curr.left is None:
                    curr.left = TreeNode(num)
                    return 'DONE'
                curr = curr.left

    def search(self, num):
        curr = self.root
        while curr:
            if curr.val == num:
                return 'YES'
            if curr.val < num:
                curr = curr.right
            elif curr.val > num:
                curr = curr.left
        return 'NO'

    def print(self, root, depth=0):
        if root:
            if root.left:
                self.print(root.left, depth + 1)
            print(f'{"." * depth}{root.val}')
            if root.right:
                self.print(root.right, depth + 1)


tree = BinaryTree()

with open('input.txt', 'r') as file:
    for line in file.readlines():
        word = line.split()
        if word[0] == 'ADD':
            print(tree.add(int(word[1])))
        elif word[0] == 'SEARCH':
            print(tree.search(int(word[1])))
        else:
            tree.print(tree.root)
