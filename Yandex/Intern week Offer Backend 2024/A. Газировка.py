def solve():
    target = lst[-1]
    ans = 0
    for i in range(n - 2, -1, -1):
        if lst[i + 1] < lst[i]:
            return -1
        ans += target - lst[i] - ans
    return ans


n = int(input())
lst = list(map(int, input().split()))
print(solve())
