n = int(input())
lst = [0] * n

for i, (x, y) in enumerate(zip(map(int, input().split()), map(int, input().split()))):
    lst[i] = (x, y, i)

useful = sorted(lst, key=lambda x: (-x[1], -x[0], x[2]))
interes = sorted(lst, key=lambda x: (-x[0], -x[1], x[2]))

was = set()
l1 = l2 = 0
ans = []
for status in map(int, input().split()):
    if not status:
        while interes[l1][2] in was:
            l1 += 1
        was.add(interes[l1][2])
        ans.append(interes[l1][2] + 1)
    else:
        while useful[l2][2] in was:
            l2 += 1
        was.add(useful[l2][2])
        ans.append(useful[l2][2] + 1)

print(*ans)
