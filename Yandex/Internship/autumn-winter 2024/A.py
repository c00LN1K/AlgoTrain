r, c = map(int, input().split())

matrix = [input() for _ in range(r)]
ans = chr(ord('z') + 1)

for i in range(r):
    for j in range(c):
        if i == 0 or matrix[i-1][j] == '#':
            t = []
            for ii in range(i, r):
                if matrix[ii][j] == '#':
                    break
                t.append(matrix[ii][j])
            if len(t) > 1:
                ans = min(ans, ''.join(t))

        if j == 0 or matrix[i][j-1] == '#':
            t = []
            for jj in range(j, c):
                if matrix[i][jj] == '#':
                    break
                t.append(matrix[i][jj])
            if len(t) > 1:
                ans = min(ans, ''.join(t))
print(ans)