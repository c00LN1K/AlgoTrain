def checkI(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = i, j
    while (y2 + 1) < n and tablo[x2][y2 + 1]:
        y2 += 1

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if not tablo[ii][jj]:
                    return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def checkC(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = i, j
    while (y2 + 1) < n and tablo[x2][y2 + 1]:
        y2 += 1

    x3, y3 = -1, -1
    x4, y4 = -1, -1
    flag = False
    for ii in range(i, x1 + 1):
        for jj in range(j, y2 + 1):
            if not tablo[ii][jj]:
                x3, y3 = ii, jj
                while (x3 + 1) <= x1 and not tablo[x3 + 1][y3]:
                    x3 += 1

                x4, y4 = ii, jj
                while (y4 + 1) <= y2 and not tablo[x4][y4 + 1]:
                    y4 += 1
                flag = True
                break
        if flag:
            break
    if not flag or not (x2 < x4 < x3 < x1 and y1 < y3 < y4 == y2):
        return False

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if x4 <= ii <= x3 and y3 <= jj <= y4:
                    if tablo[ii][jj]:
                        return False
                else:
                    if not tablo[ii][jj]:
                        return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def checkO(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = i, j
    while (y2 + 1) < n and tablo[x2][y2 + 1]:
        y2 += 1

    x3, y3 = -1, -1
    x4, y4 = -1, -1
    flag = False
    for ii in range(i, x1 + 1):
        for jj in range(j, y2 + 1):
            if not tablo[ii][jj]:
                x3, y3 = ii, jj
                while (x3 + 1) <= x1 and not tablo[x3 + 1][y3]:
                    x3 += 1

                x4, y4 = ii, jj
                while (y4 + 1) <= y2 and not tablo[x4][y4 + 1]:
                    y4 += 1
                flag = True
                break
        if flag:
            break
    if not flag or not (x2 < x4 < x3 < x1 and y1 < y3 < y4 < y2):
        return False

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if x4 <= ii <= x3 and y3 <= jj <= y4:
                    if tablo[ii][jj]:
                        return False
                else:
                    if not tablo[ii][jj]:
                        return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def checkP(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = i, j
    while (y2 + 1) < n and tablo[x2][y2 + 1]:
        y2 += 1

    x3, y3 = -1, -1
    x4, y4 = -1, -1
    x5, y5 = -1, -1
    x6, y6 = -1, -1
    flag1 = flag2 = False
    for ii in range(i, x1 + 1):
        for jj in range(j, y2 + 1):
            if not tablo[ii][jj]:
                if not flag1:
                    x3, y3 = ii, jj
                    while (x3 + 1) <= x1 and not tablo[x3 + 1][y3]:
                        x3 += 1

                    x4, y4 = ii, jj
                    while (y4 + 1) <= y2 and not tablo[x4][y4 + 1]:
                        y4 += 1
                    flag1 = True
                elif flag1 and not (x4 <= ii <= x3 and y3 <= jj <= y4):
                    x5, y5 = ii, jj
                    while (x5 + 1) <= x1 and not tablo[x5 + 1][y5]:
                        x5 += 1

                    x6, y6 = ii, jj
                    while (y6 + 1) <= y2 and not tablo[x6][y6 + 1]:
                        y6 += 1
                    flag2 = True
                    break
        if flag2:
            break

    if not flag2 or not (x2 < x4 < x3 < x6 < x5 <= x1 and y1 < y3 == y5 < y4 < y6 == y2):
        return False

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if (x4 <= ii <= x3 and y3 <= jj <= y4) or (x6 <= ii <= x5 and y5 <= jj <= y6):
                    if tablo[ii][jj]:
                        return False
                else:
                    if not tablo[ii][jj]:
                        return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def checkL(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = x1, j
    while (y2 + 1) < n and tablo[x2][y2 + 1]:
        y2 += 1
    x2 = i

    x3, y3 = -1, -1
    x4, y4 = -1, -1
    flag = False
    for ii in range(i, x1 + 1):
        for jj in range(j, y2 + 1):
            if not tablo[ii][jj]:
                x3, y3 = ii, jj
                while (x3 + 1) <= x1 and not tablo[x3 + 1][y3]:
                    x3 += 1

                x4, y4 = ii, jj
                while (y4 + 1) <= y2 and not tablo[x4][y4 + 1]:
                    y4 += 1
                flag = True
                break
        if flag:
            break
    if not flag or not (x2 == x4 < x3 < x1 and y1 < y3 < y4 == y2):
        return False

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if x4 <= ii <= x3 and y3 <= jj <= y4:
                    if tablo[ii][jj]:
                        return False
                else:
                    if not tablo[ii][jj]:
                        return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def checkH(i, j):
    x1, y1 = i, j
    while (x1 + 1) < n and tablo[x1 + 1][y1]:
        x1 += 1

    x2, y2 = i, n - 1
    while y2 > j and not tablo[x2][y2]:
        y2 -= 1

    x3, y3 = -1, -1
    x4, y4 = -1, -1
    x5, y5 = -1, -1
    x6, y6 = -1, -1
    flag1 = flag2 = False
    for ii in range(i, x1 + 1):
        for jj in range(j, y2 + 1):
            if not tablo[ii][jj]:
                if not flag1:
                    x3, y3 = ii, jj
                    while (x3 + 1) <= x1 and not tablo[x3 + 1][y3]:
                        x3 += 1

                    x4, y4 = ii, jj
                    while (y4 + 1) <= y2 and not tablo[x4][y4 + 1]:
                        y4 += 1
                    flag1 = True
                elif flag1 and not (x4 <= ii <= x3 and y3 <= jj <= y4):
                    x5, y5 = ii, jj
                    while (x5 + 1) <= x1 and not tablo[x5 + 1][y5]:
                        x5 += 1

                    x6, y6 = ii, jj
                    while (y6 + 1) <= y2 and not tablo[x6][y6 + 1]:
                        y6 += 1
                    flag2 = True
                    break
        if flag2:
            break

    if not flag2 or not (x2 == x4 < x3 < x6 < x5 == x1 and y1 < y3 == y5 < y4 == y6 < y2):
        return False

    for ii in range(n):
        for jj in range(n):
            if x2 <= ii <= x1 and y1 <= jj <= y2:
                if (x4 <= ii <= x3 and y3 <= jj <= y4) or (x6 <= ii <= x5 and y5 <= jj <= y6):
                    if tablo[ii][jj]:
                        return False
                else:
                    if not tablo[ii][jj]:
                        return False
            else:
                if tablo[ii][jj]:
                    return False
    return True


def solve():
    for i in range(n):
        for j in range(n):
            if tablo[i][j]:
                if checkI(i, j):
                    return 'I'
                elif checkC(i, j):
                    return 'C'
                elif checkO(i, j):
                    return 'O'
                elif checkL(i, j):
                    return 'L'
                elif checkH(i, j):
                    return 'H'
                elif checkP(i, j):
                    return 'P'
                else:
                    return 'X'
    return 'X'


n = 2 * int(input())
tablo = [[False] * n for i in range(n)]
for i in range(n // 2):
    for j, val in enumerate(input()):
        if val == '#':
            tablo[2 * i][2 * j] = True
            tablo[2 * i][2 * j + 1] = True
            tablo[2 * i + 1][2 * j] = True
            tablo[2 * i + 1][2 * j + 1] = True
print(solve())
