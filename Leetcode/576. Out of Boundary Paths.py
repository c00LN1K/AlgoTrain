from collections import deque


def findPaths(m, n, maxMove, startRow, startColumn):
    dp = [[0] * n for _ in range(m)]
    dp[startRow][startColumn] = 1  # используем dp, чтобы посчитать количество путей для каждой клетки
    # но также надо считать промежуточные значение (т.к. можно выйти из сетки при любом ходе (главное чтобы это была граница))
    ans = 0
    for _ in range(1, maxMove + 1):
        t = [[0] * n for _ in range(m)]
        # каждый ход создаем новый временный массив (в нем будем хранить количество путей для каждой ячейки при очередном ходе)
        for i in range(0, m):
            for j in range(0, n):
                # проверка на крайние значения (если это край, то прибавляем к счетчику количество путей для ячейки на данный момент)
                if i == 0: ans += dp[i][j]
                if j == 0: ans += dp[i][j]
                if i == (m - 1): ans += dp[i][j]
                if j == (n - 1): ans += dp[i][j]

                # делаем пересчет путей (количество путей в новой ячейке = сумме путей в ячейках, из которых можно в неё попасть)
                t[i][j] = (dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < (m - 1) else 0) + \
                          (dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < (n - 1) else 0)
        # обновляем значение dp (чтобы сбросить значения dp предыдущего хода)
        dp = t
    return ans % (10 ** 9 + 7)


print(findPaths(3, 3, 3, 1, 0))


def bfs(m, n, maxMove, startRow, startColumn):
    if maxMove == 0:
        return 0
    d = deque()
    d.append([startRow, startColumn, maxMove])
    ans = 0
    while d:
        pos = d.popleft()
        for i, j in zip([pos[0] - 1, pos[0] + 1, pos[0], pos[0]], [pos[1], pos[1], pos[1] - 1, pos[1] + 1]):
            if (0 > i or i >= m) or (0 > j or j >= n):
                ans += 1
            elif pos[2] > 1:
                d.append((i, j, pos[2] - 1))
    return ans

    # return bfs(m, n, maxMove - 1, startRow - 1, startColumn) + \
    #     bfs(m, n, maxMove - 1, startRow, startColumn - 1) + \
    #     bfs(m, n, maxMove - 1, startRow + 1, startColumn) + \
    #     bfs(m, n, maxMove - 1, startRow, startColumn + 1)
