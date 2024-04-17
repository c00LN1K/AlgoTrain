from collections import deque


def bfs(start, end, pole):
    d = deque()
    d.append((*start, 0, 'K'))
    d_moves = {
        'K': [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)],
        'G': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    }
    seen = set()
    while d:
        i, j, moves, figure = d.popleft()
        seen.add((i, j, figure))
        for di, dj in d_moves[figure]:
            ii, jj = i + di, j + dj
            if 0 <= ii < len(pole) and 0 <= jj < len(pole):
                if (ii, jj) == end:
                    return moves + 1
                new_figure = pole[ii][jj] if pole[ii][jj] in d_moves else figure
                if (ii, jj, new_figure) not in seen:
                    d.append((ii, jj, moves + 1, new_figure))
    return -1


n = int(input())
pole = []
for i in range(n):
    t = input()
    for j, val in enumerate(t):
        if val == 'S':
            start = i, j
        elif val == 'F':
            end = i, j
    pole.append(t)
print(bfs(start, end, pole))
