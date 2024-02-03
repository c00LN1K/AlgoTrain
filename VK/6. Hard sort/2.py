import re


def merge_list(left, right):
    i, j = 0, 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i][-1] < right[j][-1] or (left[i][-1] == right[j][-1] and left[i][1] < right[j][1]):
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
books = [re.split('\s*"\s*', input()) for i in range(n)]
print(books)
for book in merge_sort(books):
    print(book[0], '"' + book[1] + '"', book[-1])
