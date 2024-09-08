from collections import defaultdict

n, d = map(int, input().split())
line = []
points = [int(p) for p in input().split()]
dd = defaultdict(int)

for p in points:
    line.append((p - d, 0))
    line.append((p + d, 1))

line.sort()

count = 0


print(dd)