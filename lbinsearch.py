lst = [3, 3, 3, 3, 3, 3, 3, 7, 8]


def left_binary_search(target):
    left, right = 0, len(lst) - 1

    while left < right:
        mid = (left + right) // 2
        if lst[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


print(left_binary_search(5))
