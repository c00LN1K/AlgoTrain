from collections import defaultdict

n, k = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
d = defaultdict(int)
ans = [0, n]

for right in range(n):
    d[lst[right]] += 1
    while len(d) == k:
        if ans[1] - ans[0] > (right - left):
            ans = [left, right]
        d[lst[left]] -= 1
        if d[lst[left]] == 0:
            d.pop(lst[left])
        left += 1

print(*map(lambda x: x + 1, ans))
