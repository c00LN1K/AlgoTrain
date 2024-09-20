from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
n = int(input())
parents = defaultdict(list)
children = set()

for i in range(n-1):
    child, parent = input().split()
    parents[parent].append(child)
    children.add(child)

root = (set(parents.keys()) - children).pop()
d = {}

def count_children(root):
    count = 0
    for child in parents[root]:
        count += count_children(child)
    d[root] = count
    return count + 1

count_children(root)
for parent, count in sorted(d.items()):
    print(parent, count)


