n = int(input())


def is_good(k):
    i = 1
    t = k * i
    while k:
        if t > n:
            return False
        i += 1
        k -= 1
        t += (k + 1) * i

    return True


l, r = 0, int((n ** 0.5) + 1)

while l < r:
    mid = (l + r + 1) // 2
    if (((mid - 1) + 3) * ((mid - 1) ** 2 + 6 * (mid - 1) + 2) // 6) <= n:
        l = mid
    else:
        r = mid - 1

print(l)

# t = k
# i = k
# q = 1
# while q < k // 2:
#     if t > n:
#         return False
#     t += 2 * ((q + 1) * i)
#     i -= 1
#     q += 1
# return True
