n, m, k = map(int, input().split())
prefix = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    prefix[i][0] = prefix[i - 1][-1]
    for j, el in enumerate(map(int, input().split()), 1):
        prefix[i][j] = prefix[i][j - 1] + el
    prefix[i][0] = 0
print(*prefix, sep='\n')

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for x in range(x1, x2 + 1):
        res += prefix[x][y2] - prefix[x][y1-1]
        print(res)
    print(res)
