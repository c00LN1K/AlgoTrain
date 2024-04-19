n = int(input())
d = {}
for _ in range(n):
    directory = input().split('/')
    prev = d
    for i in directory:
        prev = prev.setdefault(i, {})


def dfs(root, spaces=0):
    for dir in sorted(root.keys()):
        print(spaces * ' ' + dir)
        dfs(root[dir], spaces + 2)


dfs(d)
