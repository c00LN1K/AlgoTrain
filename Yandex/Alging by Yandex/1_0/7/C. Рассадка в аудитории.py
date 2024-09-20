n, d = map(int, input().split())
line = []
points = [int(p) for p in input().split()]


for i, p in enumerate(points):
    line.append((p, 0, i))
    line.append((p + d, 1, i))

line.sort()
free_tickets = set()
total_tickets = 0
dd = {}

for p, t, i in line:
    if t == 0:
        if not free_tickets:
            total_tickets += 1
            free_tickets.add(total_tickets)
        dd[i] = free_tickets.pop()
    elif t == 1:
        free_tickets.add(dd[i])

print(total_tickets)
print(*[dd[i] for i in range(n)])
