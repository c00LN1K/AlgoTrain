n, k = map(int, input().split())
cars = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + cars[i]

l = 0
ans = 0
for r in range(1, n + 1):
    while prefix[r] - prefix[l] >= k:
        if prefix[r] - prefix[l] == k:
            ans += 1
        l += 1

print(ans)
