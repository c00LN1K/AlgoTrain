n, i, j = map(int, input().split())
i, j = min(i, j), max(j, i)
print(min(j - i - 1, i + n - j - 1))