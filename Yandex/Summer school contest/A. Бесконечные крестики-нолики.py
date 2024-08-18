def check_win(x, y):
    fig = pole[(x, y)]
    shifts = [-1, 1] * 4
    vertical = horizontal = left_diagonal = right_diagonal = 1
    while any(map(lambda k: k < 5, shifts)):
        for i in range(2):
            if abs(shifts[i]) < 5 and pole.get((x + shifts[i], y)) == fig:
                vertical += 1
                shifts[i] += 1 * 1 if i % 2 else -1
            else:
                shifts[i] = 5

        for i in range(2, 4):
            if abs(shifts[i]) < 5 and pole.get((x, y + shifts[i])) == fig:
                horizontal += 1
                shifts[i] += 1 * 1 if i % 2 else -1
            else:
                shifts[i] = 5

        for i in range(4, 6):
            if abs(shifts[i]) < 5 and pole.get((x + shifts[i], y + shifts[i])) == fig:
                right_diagonal += 1
                shifts[i] += 1 * 1 if i % 2 else -1
            else:
                shifts[i] = 5

        for i in range(6, 8):
            if abs(shifts[i]) < 5 and pole.get((x + shifts[i], y - shifts[i])) == fig:
                left_diagonal += 1
                shifts[i] += 1 * 1 if i % 2 else -1
            else:
                shifts[i] = 5

    return any(map(lambda el: el >= 5, [horizontal, vertical, left_diagonal, right_diagonal]))


def main(n, pole):
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        pole[(x, y)] = i % 2
        if check_win(x, y):
            if n == i:
                return 'First' if pole[(x, y)] else 'Second'
            return 'Inattention'
    return 'Draw'


if __name__ == '__main__':
    n = int(input())
    pole = {}
    print(main(n, pole))
