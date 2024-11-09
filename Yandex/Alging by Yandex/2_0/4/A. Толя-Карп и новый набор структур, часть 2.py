from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    color, num = map(int, input().split())
    d[color] += num
for color, num in sorted(d.items()):
    print(color, num)