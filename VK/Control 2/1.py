n = int(input())
lst = list(map(int, input().split()))

d = {}

for i in lst:
    d[i] = d.setdefault(i, 0) + 1

max_key = max(d.keys(), key=lambda x: d[x])
print(max_key if (d[max_key] > n / 2) else -1)
