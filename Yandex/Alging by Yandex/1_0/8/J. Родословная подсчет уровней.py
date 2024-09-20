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

def count_levels(root, count):
    d[root] = count
    for child in parents[root]:
        count_levels(child, count + 1)
    d[root] = count
    return count + 1

count_levels(root, 0)
for parent, level in sorted(d.items()):
    print(parent, level)

