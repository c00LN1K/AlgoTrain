t, d, n = map(int, input().split())
ans = set()
ans.add((0, 0))

for i in range(n):
    for x, y in ans.copy():
        for dx in range(t + 1):
            for dy in range(t + 1):
                if dx + dy <= t:
                    ans.add((x + dx, y + dy))
                    ans.add((x - dx, y + dy))
                    ans.add((x + dx, y - dy))
                    ans.add((x - dx, y - dy))

    x, y = map(int, input().split())
    moves = set()
    for dx in range(d + 1):
        for dy in range(d + 1):
            if dx + dy <= d:
                for dd in range(t):
                    moves.add((x + dx, y + dy))
                    moves.add((x - dx, y + dy))
                    moves.add((x + dx, y - dy))
                    moves.add((x - dx, y - dy))
    ans = moves

print(len(ans))
for el in ans:
    print(*el)


