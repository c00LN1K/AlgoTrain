import timeit

n = int(input())
lst = list(map(int, input().split()))
needle = int(input())


# Найти needle в массиве lst или где он мог гипотетически быть
def triple_search():
    left = 0
    right = n - 1

    while left <= right:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        if lst[m1] == needle:
            return m1
        if lst[m2] == needle:
            return m2

        if lst[m2] < needle:
            left = m2 + 1
        elif needle < lst[m1]:
            right = m1 - 1
        else:
            left, right = m1 + 1, m2 - 1

    return left


def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == needle:
            return mid
        if lst[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1
    return left


def e_search():
    border = 1
    while 0 < border < n and lst[border] <= needle:
        if lst[border] == needle:
            return border
        border *= 2
    if n - 1 < border:
        return binary_search(border // 2, n - 1)
    else:
        return binary_search(border // 2, border)


def interpol_search():
    left = 0
    right = n - 1
    while left <= right:
        pass


print(timeit.timeit(triple_search, number=10000))
# print(timeit.timeit(binary_search, number=10000))
print(timeit.timeit(e_search, number=10000))
print(triple_search())
print(binary_search(0, n - 1))
print(e_search())
