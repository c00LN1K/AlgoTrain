from collections import defaultdict

d = defaultdict(int)
for el in map(int, input().split()):
    d[el] += 1

ans = []
for key, val in d.items():
    if val == 1:
        ans.append(key)
print(*ans)