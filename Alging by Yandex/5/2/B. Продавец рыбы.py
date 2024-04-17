n, days = map(int, input().split())
fishes = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    t = fishes[i]
    ans = max(ans, max(fishes[i + 1:i + days + 1]) - t)

print(ans)
