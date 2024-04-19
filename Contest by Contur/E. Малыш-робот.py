n = int(input())

polex = {}
poley = {}
stops = set()

for i in range(n):
    x, y = map(int, input().split())
    polex[x] = polex.setdefault(x, set()) | {y}
    poley[y] = poley.setdefault(y, set()) | {x}


def solve():
    x, y = 0, 0
    q = int(input())
    for i in range(q):
        action, steps = input().split()
        steps = int(steps)
        if action == 'U':
            if x in polex:
                if set(range(y, y + steps + 1)) & polex[x]:
                    return f'Stop {i + 1}'
            y += steps

        elif action == 'D':
            if x in polex:
                if set(range(y, y - steps - 1, -1)) & polex[x]:
                    return f'Stop {i + 1}'
            y -= steps
        elif action == 'L':
            if y in poley:
                if set(range(x, x - steps - 1, -1)) & polex[y]:
                    return f'Stop {i + 1}'
            x -= steps
        else:
            if y in poley:
                if set(range(x, x + steps + 1)) & polex[y]:
                    return f'Stop {i + 1}'
            x += steps
    return 'Complete'


print(solve())
