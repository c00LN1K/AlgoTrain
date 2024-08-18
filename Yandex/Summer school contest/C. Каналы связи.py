import math


def build_lines(cost):
    built = []
    new_lines = []
    for i in range(len(lines)):
        new_lines.append(lines[i].copy())

    for i in range(len(suggests)):
        x, y, t, c = suggests[i]
        if c <= cost:
            built.append(i + 1)
            new_lines[x - 1][y - 1] = t
            new_lines[y - 1][x - 1] = t
    return new_lines, built


def check_requires(ways):
    for i in range(len(requires)):
        x, y, t = requires[i]
        if ways[x - 1][y - 1] > t:
            return False
    return True


def floyd(ways):
    for i in range(len(ways)):
        for j in range(len(ways)):
            for q in range(len(ways)):
                ways[i][j] = min(ways[i][j], ways[i][q] + ways[q][j])
    return ways


def main(l, r):
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        new_lines, built = build_lines(mid)
        shortest_ways = floyd(new_lines)
        if check_requires(shortest_ways):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[math.inf] * n for _ in range(n)]
    for i in range(m):
        x, y, t = map(int, input().split())
        lines[x - 1][y - 1] = t
        lines[y - 1][x - 1] = t

    k = int(input())
    suggests = []
    l, r = 0, 0
    for i in range(k):
        suggests.append(tuple(map(int, input().split())))
        r = max(r, suggests[-1][-1])

    p = int(input())
    requires = []
    for i in range(p):
        requires.append(tuple(map(int, input().split())))

    result = main(l, r + 10)
    if result < 1:
        print(result)
    else:
        ans = []
        for i in range(len(suggests)):
            x, y, t, c = suggests[i]
            if c <= result:
                ans.append(i + 1)
        print(len(ans))
        print(*ans)
