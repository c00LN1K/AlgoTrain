import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


def count_depth(root, depth=0):
    depths[root] = depth
    for ch in children[root]:
        count_depth(ch, depth + 1)


def find_common_parent(target1, target2):
    if target1 == target2:
        ans.append(target1)
    elif depths[target1] < depths[target2]:
        find_common_parent(target1, parents[target2])
    elif depths[target1] > depths[target2]:
        find_common_parent(parents[target1], target2)
    else:
        find_common_parent(parents[target1], parents[target2])


with open('input.txt') as file:
    ans = []
    n = int(file.readline())
    children = defaultdict(list)
    parents = {}
    for _ in range(n - 1):
        child, parent = file.readline().split()
        children[parent].append(child)
        parents[child] = parent
    root = set(children.keys()) - set(parents.keys())
    if root:
        root = tuple(root)[0]
        depths = {}
        count_depth(root)
    for line in file.readlines():
        line = line.strip('\n')
        if not line:
            continue
        first, second = line.split()
        find_common_parent(first, second)
    print(*ans, sep='\n')
