n, m = map(int, input().split())
lst = []
for pos in map(int, input().split()):
    lst.append((pos, 1, -1))

ans = [0] * m
for i in range(m):
    l, r = map(int, input().split())
    lst.append((l, 0, i))
    lst.append((r, 2, i))

lst.sort()
d = {}
count = 0
for pos, type, index in lst:
    if type == 0:
        d[index] = count
    elif type == 1:
        count += 1
    elif type == 2:
        ans[index] = count - d[index]

print(*ans)
