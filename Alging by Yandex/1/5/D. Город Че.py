n, k = map(int, input().split())
dist = list(map(int, input().split()))
l = 0
ans = 0
for r in range(n):
    while (dist[r] - dist[l]) > k:
        ans += (n - r)
        l += 1
print(ans)
