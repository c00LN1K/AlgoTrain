def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def solve():
    left, right = -1, 1
    while f(left) * f(right) >= 0:
        left *= 10
        right *= 10
    while right - left > 10 ** -8:
        mid = (left + right) / 2
        if f(mid) == 0:
            return mid
        if f(mid) * f(left) < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

a, b, c, d = map(float, input().split())
print(solve())