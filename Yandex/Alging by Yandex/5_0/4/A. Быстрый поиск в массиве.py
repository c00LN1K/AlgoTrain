n = int(input())
lst = sorted(map(int, input().split()))


def right_binary_search(target):
    left, right = 0, len(lst) - 1

    while (left + 1) < right:
        mid = (left + right) // 2
        if lst[mid] <= target:
            left = mid
        else:
            right = mid

    if lst[right] == target:
        return right
    elif lst[left] == target:
        return left
    else:
        if target < lst[left]:
            return left
        if lst[left] < target < lst[right]:
            return right
        return right


def left_binary_search(target):
    left, right = 0, len(lst) - 1

    while (left + 1) < right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid
        else:
            right = mid

    if lst[left] == target:
        return left
    elif lst[right] == target:
        return right
    else:
        if target < lst[left]:
            return left
        if lst[left] < target < lst[right]:
            return left
        return right


q = int(input())
ans = []
for i in range(q):
    l, r = map(int, input().split())

    if l <= lst[0]:
        ll = 0
    else:
        ll = left_binary_search(l)

    if lst[-1] <= r:
        rr = n - 1
    else:
        rr = right_binary_search(r)

    ans.append(rr - ll - 1 + int(l <= lst[ll]) + int(lst[rr] <= r))

print(*ans)