def check(length):
    res = 1
    right = lst[0] + length
    for i in range(1, n):
        if lst[i] > right:
            right = lst[i] + length
            res += 1
    return res


n, k = map(int, input().split())
lst = sorted(map(int, input().split()))
l, r = 0, abs(lst[0]) + abs(lst[-1])

while l < r:
    mid = (l + r) // 2
    if check(mid) <= k:
        r = mid
    elif check(mid) > k:
        l = mid + 1
print(l)