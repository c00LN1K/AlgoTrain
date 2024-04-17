def turn_left(lst):
    l = []
    for j in range(len(lst) - 1, -1, -1):
        t = []
        for i in range(len(lst)):
            t.append(lst[i][j])
        l.append(t)
    return l


def turn_right(lst):
    l = []
    for j in range(len(lst)):
        t = []
        for i in range(len(lst) - 1, -1, -1):
            t.append(lst[i][j])
        l.append(t)
    return l


def find_replace(d, lst, new_lst, i, j):
    for ii, jj in d[new_lst[i][j]].copy():
        d[new_lst[i][j]].discard((ii, jj))
        if lst[ii][jj] != new_lst[ii][jj]:
            d[lst[i][j]].discard((i, j))
            d[lst[i][j]].add((ii, jj))
            return ii, jj


n, turn = input().split()
n = int(n)
lst = []
d = {}
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        d[t[j]] = d.setdefault(t[j], set())
        d[t[j]].add((i, j))
    lst.append(t)

new_lst = turn_left(lst) if turn == 'L' else turn_right(lst)

ans = []
for i in range(n):
    for j in range(n):
        if lst[i][j] != new_lst[i][j]:
            ii, jj = find_replace(d, lst, new_lst, i, j)
            lst[i][j], lst[ii][jj] = lst[ii][jj], lst[i][j]
            ans.append((i, j, ii, jj))

print(len(ans))
for el in ans:
    print(*el)
print(lst, new_lst)

