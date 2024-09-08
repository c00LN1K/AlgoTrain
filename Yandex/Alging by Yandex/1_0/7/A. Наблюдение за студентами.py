n, m = map(int, input().split())
desks = []

for _ in range(m):
    st, end = map(int, input().split())
    desks.append((st, 0))
    desks.append((end, 1))

desks.sort()
count = left = ans = 0

for pos, type in desks:
    if type == 0:
        if count == 0:
            left = pos
        count += 1
    elif type == 1:
        count -= 1
        if count == 0:
            ans += pos - left + 1

print(n - ans)