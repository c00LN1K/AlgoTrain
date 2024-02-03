def merge_list(left, right):
    i, j = 0, 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    return lst + left[i:] + right[j:]


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge_list(left, right)


n = int(input())
print(*merge_sort(list(map(int, input().split()))))
