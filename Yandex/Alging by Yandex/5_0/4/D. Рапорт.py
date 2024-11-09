w, n, m = map(int, input().split())


def check(lst, line):
    t = 0
    k = 1
    for i in range(len(lst)):
        if t + lst[i] <= line:
            t += lst[i] + 1
        else:
            if lst[i] > line:
                return float('inf')
            t = lst[i] + 1
            k += 1
    return k


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
left, right = 1, w - 1
while (left + 1) < right:
    mid = (left + right) // 2
    if check(lst1, mid) > check(lst2, w - mid):
        left = mid
    else:
        right = mid

ans1 = max(check(lst1, left), check(lst2, w - left))
ans2 = max(check(lst1, right), check(lst2, w - right))

print(min(ans1, ans2))

# children = {}
#
#
# def check(line):
#     if line in children:
#         return children[line]
#     k = 1
#     t = 0
#     for i in range(len(lst1)):
#         if t + lst1[i] <= line:
#             t += lst1[i] + 1
#         else:
#             if lst1[i] > line:
#                 children[line] = float('-inf')
#                 return children[line]
#             t = lst1[i] + 1
#             k += 1
#     k1 = 1
#     t = 0
#     line1 = w - line
#     for i in range(len(lst2)):
#         if t + lst2[i] <= line1:
#             t += lst2[i] + 1
#         else:
#             if lst2[i] > line1:
#                 children[line] = float('inf')
#                 return children[line]
#             t = lst2[i] + 1
#             k1 += 1
#     children[line] = max(k, k1)
#     return children[line]
#
#
# # left, right = max(lst1), w - max(lst2)
# left, right = 1, w - 1
# ans = 0
# if left == right:
#     print(check(left))
# else:
#     while (left + 1) < right:
#         mid = (left + right) // 2
#         c1 = check(mid)
#
#         if c1 == float('-inf'):
#             left = mid + 1
#         elif c1 == float('inf'):
#             right = mid - 1
#         else:
#             c2 = check(mid + 1)
#             if c1 < c2:
#                 right = mid - 1
#             elif c1 > c2:
#                 left = mid + 1
#             else:
#                 # if mid - left > right - mid:
#                 #     left = mid
#                 # else:
#                 #     right = mid
#     # print(min(children.values(), key=lambda x: float('inf') if x == float('-inf') else x))
