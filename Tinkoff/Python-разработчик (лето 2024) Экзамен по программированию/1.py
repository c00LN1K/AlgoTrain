def solve(n: int, lst: list):
    if n < 7:
        return -1
    ans = -1
    number_fives = 0
    left = 0
    for right in range(n):
        if lst[right] == 5:
            number_fives += 1
        elif lst[right] in (2, 3):
            left = right + 1
            number_fives = 0
        if (right - left + 1) == 7:
            ans = max(ans, number_fives)
            if lst[left] == 5:
                number_fives -= 1
            left += 1
    return ans


n = int(input())
lst = list(map(int, input().split()))
print(solve(n, lst))
