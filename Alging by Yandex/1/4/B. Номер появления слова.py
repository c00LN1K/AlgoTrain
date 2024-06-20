from sys import stdin
from collections import defaultdict

d = defaultdict(int)
ans = []

for row in stdin:
    for word in row.split():
        d[word] += 1
print(sorted(dict(sorted(d.items(), reverse=True)).items(), key=lambda x: x[1])[-1][0])
