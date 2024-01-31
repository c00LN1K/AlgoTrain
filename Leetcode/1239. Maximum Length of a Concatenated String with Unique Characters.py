from itertools import combinations


def maxLength(arr):
    ans = 0
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            s = ''.join(comb)
            if ans < len(s) and len(set(s)) == len(s):
                ans = len(s)
    return ans


print(maxLength(["un","iq","ue"]))
