n, m = map(int, input().split())

line = []
d = {}

for _ in range(n):
    st, end = sorted(map(int, input().split()))
    line.append((st, -1))
    line.append((end, 1))

points =[int(point) for point in input().split()]
for point in points:
    d.setdefault(point, 0)
    line.append((point, 0))

line.sort()
count = 0

for pos, type in line:
    if type == -1:
        count += 1
    elif type == 1:
        count -= 1
    else:
        d[pos] = count

print(*[d[point] for point in points])