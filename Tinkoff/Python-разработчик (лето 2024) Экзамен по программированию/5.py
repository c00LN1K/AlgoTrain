n = int(input())
lst = [[0] * 3]
d = {'.': 0, 'C': 1, 'W': -1}
for i in range(n):
    lst.append([d[el] for el in input()])

i = 1
while i <= n:
    for j in range(3):
        if lst[i][j] != -1:
            moves = [lst[i - 1][jj] for jj in range(max(0, j - 1), min(j + 2, 3)) if lst[i - 1][jj] != -1]
            if moves:
                lst[i][j] += max(moves)
            else:
                lst[i][j] = -1
    if not any(map(lambda x: x != -1, lst[i])):
        break
    i += 1
print(max(lst[i - 1]))
