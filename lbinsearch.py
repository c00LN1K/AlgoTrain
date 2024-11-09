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


print(left_binary_search(3))

def right_binary_search(target):
    left, right = 0, len(lst) - 1

    while left < right:
        mid = (left + right + 1) // 2
        if lst[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left

print(right_binary_search(3))