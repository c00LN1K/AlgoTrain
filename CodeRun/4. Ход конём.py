n, m = map(int, input().split())


def moves(curr_i, curr_j):
    if curr_i > n or curr_j > m:
        return 0
    elif curr_i == n and curr_j == m:
        return 1
    else:
        return moves(curr_i + 2, curr_j + 1) + moves(curr_i + 1, curr_j + 2)


print(moves(1, 1))
