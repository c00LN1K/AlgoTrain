n, k = map(int, input().split())
lst = list(map(int, input().split()))
l = 0
curr = 0
ans = 0
for r in range(n):
    curr += lst[r]
    while curr > k:
        curr -= lst[l]
        l += 1
    if curr == k:
        ans += 1
print(ans)