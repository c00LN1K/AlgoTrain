t, d, n = map(int, input().split())

pos = (0, 0, 0, 0)

for i in range(n):
    x, y = map(int, input().split())
    pos = max(pos[0] - t, x + y - d), min(pos[1] + t, x + y + d), max(pos[2] - t, x - y - d), min(pos[3] + t, x - y + d)

ans = []
for x_plus_y in range(pos[0], pos[1] + 1):
    for x_minus_y in range(pos[2], pos[3] + 1):
        if (x_plus_y + x_minus_y) % 2 == 0:
            x = (x_plus_y + x_minus_y) // 2
            y = x_plus_y - x
            ans.append((x, y))

print(len(ans))
for el in ans:
    print(*el)
