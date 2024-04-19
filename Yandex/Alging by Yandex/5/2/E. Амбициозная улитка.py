n = int(input())
pos_berries = []
neg_berries = []
positive_summ = 0
max_negative = [0, 0]
good_berrie = [0, 0]

for i in range(n):
    up, down = map(int, input().split())
    if up - down > 0:
        pos_berries.append((i + 1, up, down))
        positive_summ += up - down
    else:
        neg_berries.append((i + 1, up))

maxx = positive_summ
for i, up, down in pos_berries:
    t = positive_summ - (up - down)
    if t + up > maxx:
        good_berrie = [i, down]
        maxx = t + up

for i, up in neg_berries:
    if max_negative[1] < up:
        max_negative = [i, up]

if pos_berries:
    pos_berries = [i for i, _, _ in pos_berries if i != good_berrie[0]]
    if neg_berries:
        print(max(maxx, maxx - good_berrie[1] + max_negative[1]))
        print(*pos_berries + [good_berrie[0]] + [max_negative[0]] + [i for i, _ in neg_berries if i != max_negative[0]])
    else:
        print(maxx)
        print(*pos_berries + [good_berrie[0]])
else:
    print(max_negative[1])
    print(*[max_negative[0]] + [i for i, _ in neg_berries if i != max_negative[0]])
