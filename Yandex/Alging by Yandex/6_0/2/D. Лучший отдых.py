n, k = map(int, input().split())
lst = sorted(map(int, input().split()))

r = 0
ans = 0
for l in range(n):
    while r < n and lst[r] - lst[l] <= k:
        r += 1
    ans = max(ans, r - l)
print(ans)
