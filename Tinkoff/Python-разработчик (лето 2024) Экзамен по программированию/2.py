n, m = map(int, input().split())
lst = [input().split() for i in range(n)]

for i in range(m):
    t = []
    for j in range(n - 1, -1, -1):
        t.append(lst[j][i])
    print(' '.join(t))
