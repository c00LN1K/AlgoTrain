m = int(input())

n = int(input())
lst = []
for i in range(n):
    l, r = map(int, input().split())
    lst.append((l, 0, i))
    lst.append((r, 1, i))

lst.sort()
status = [1] * n
count = []

for pos, type, index in lst:
    if type == 0:
        if count:
            k = max(count)
            if k > index:
                status[index] = 0
            else:
                status[k] = 0
        count.append(index)
    elif type == 1:
        count.remove(index)
print(status.count(1))
