n = int(input())
lst = list(map(int, input().split()))
m, k = map(int, input().split())
prefix = [0] * n

l = n - 1
t = k
for r in range(n - 1, -1, -1):
    if r + 1 < n and lst[r] == lst[r + 1]:
        t = min(k, t + 1)
    while l > 0 and (lst[l - 1] < lst[l] or (lst[l - 1] == lst[l] and t)):
        if lst[l - 1] == lst[l]:
            t -= 1
        l -= 1
    prefix[r] = l + 1
    l = min(l, r - 1)

ans = [0] * m
for i, index in enumerate(map(int, input().split())):
    ans[i] = prefix[index - 1]
print(*ans)
