n, dist = map(int, input().split())
lst = list(map(int, input().split()))

l = 0
ans = 0
for r in range(n):
    while lst[r] - lst[l] > dist:
        ans += n - r
        l += 1
print(ans)
