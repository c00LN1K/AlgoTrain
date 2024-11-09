def left_binary_search(target):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = (l + r) // 2
        if target <= lst[mid]:
            r = mid
        else:
            l = mid + 1
    if lst[l] != target:
        l = -1
    return l + 1


def right_binary_search(target):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if lst[mid] <= target:
            l = mid
        else:
            r = mid - 1
    if lst[l] != target:
        l = -1
    return l + 1

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
for el in map(int, input().split()):
    print(left_binary_search(el), right_binary_search(el))