def left_binary_search(target):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = (l + r) // 2
        if target <= lst[mid]:
            r = mid
        else:
            l = mid + 1
    if lst[l] < target:
        l += 1
    return l


def right_binary_search(target):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if lst[mid] <= target:
            l = mid
        else:
            r = mid - 1
    if lst[l] <= target:
        l += 1
    return l


n = int(input())
lst = sorted(map(int, input().split()))
k = int(input())
ans = []
for _ in range(k):
    l, r = map(int, input().split())
    left_index = left_binary_search(l)
    right_index = right_binary_search(r)
    print(left_index, right_index)
    ans.append(max(right_index - left_index, 0))
print(*ans)
