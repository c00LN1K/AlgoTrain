def exp_search(start, end, find):
    border = 1
    while start <= border <= end and lst[border] <= find:
        if lst[border] == find:
            return border,
        border *= 2

    if end < border:
        return border // 2, end
    return border // 2, border


n = int(input())
lst = list(map(int, input().split()))
find = int(input())
print(*exp_search(0, n - 1, find))


