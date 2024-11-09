import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


def count_max_distance(root, s):
    global ans
    res1 = res2 = 0
    for child in d[root]:
        if child not in s:
            res = count_max_distance(child, s | {child})
            if res > res1:
                res1, res2 = res, res1
            elif res >= res2:
                res2 = res
    ans = max(ans, res1 + res2 + 1)
    return res1 + 1


n = int(input())
d = defaultdict(list)
ans = 1
if n > 1:
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        d[parent].append(child)
        d[child].append(parent)
    count_max_distance(parent, {parent})
print(ans)
