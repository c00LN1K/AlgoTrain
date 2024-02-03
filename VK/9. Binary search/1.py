n = int(input())
prices = list(map(int, input().split()))
find = int(input())


def binary_search():
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if prices[mid] == find:
            return 'true'
        elif prices[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    return 'false'


print(binary_search())
