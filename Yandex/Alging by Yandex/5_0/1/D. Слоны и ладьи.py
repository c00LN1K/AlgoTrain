from pprint import pprint

l = []
figures = []
for i in range(8):
    t = list(input()[:8])
    for j in range(8):
        if t[j] != '*':
            figures.append((t[j], i, j))
    l.append(t)

ans = 64

for fig, i, j in figures:
    ans -= 1
    if fig == 'R':
        for j1 in range(j + 1, 8):
            if l[i][j1] in ['R', 'B']:
                break
            elif l[i][j1] == 'X':
                continue
            ans -= 1
            l[i][j1] = 'X'
        for j1 in range(j - 1, -1, -1):
            if l[i][j1] in ['R', 'B']:
                break
            elif l[i][j1] == 'X':
                continue
            ans -= 1
            l[i][j1] = 'X'

        for i1 in range(i + 1, 8):
            if l[i1][j] in ['R', 'B']:
                break
            elif l[i1][j] == 'X':
                continue
            ans -= 1
            l[i1][j] = 'X'

        for i1 in range(i - 1, -1, -1):
            if l[i1][j] in ['R', 'B']:
                break
            elif l[i1][j] == 'X':
                continue
            ans -= 1
            l[i1][j] = 'X'
    else:
        for d in range(1, 8):
            i1, j1 = i + d, j + d
            if 0 <= i1 < 8 and 0 <= j1 < 8:
                if l[i1][j1] in ['R', 'B']:
                    break
                elif l[i1][j1] == '*':
                    ans -= 1
                    l[i1][j1] = 'X'
            else:
                break

        for d in range(1, 8):
            i1, j1 = i + d, j - d
            if 0 <= i1 < 8 and 0 <= j1 < 8:
                if l[i1][j1] in ['R', 'B']:
                    break
                elif l[i1][j1] == '*':
                    ans -= 1
                    l[i1][j1] = 'X'
            else:
                break

        for d in range(1, 8):
            i1, j1 = i - d, j + d
            if 0 <= i1 < 8 and 0 <= j1 < 8:
                if l[i1][j1] in ['R', 'B']:
                    break
                elif l[i1][j1] == '*':
                    ans -= 1
                    l[i1][j1] = 'X'
            else:
                break

        for d in range(1, 8):
            i1, j1 = i - d, j - d
            if 0 <= i1 < 8 and 0 <= j1 < 8:
                if l[i1][j1] in ['R', 'B']:
                    break
                elif l[i1][j1] == '*':
                    ans -= 1
                    l[i1][j1] = 'X'
            else:
                break
print(ans)
pprint(l)