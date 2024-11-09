a, k, b, m, x = map(int, input().split())

l, r = 0, x + 1

while l < r:
    mid = (l + r) // 2
    total = a * mid - a * (mid // k) + b * mid - b * (mid // m)
    if total >= x:
        r = mid
    else:
        l = mid + 1

print(l)
