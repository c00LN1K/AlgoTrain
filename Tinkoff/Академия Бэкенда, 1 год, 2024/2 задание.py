d = {val: i for i, val in enumerate(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'], 1)}

dates = {0, 29}
for i in range(4):
    t = input().split()
    for val in t:
        dates.add(d[val] + i * 7)

if len(dates) == 30:
    print(*[0, 0])
else:
    ans = []
    lst = sorted(dates)
    for i in range(len(lst) - 1):
        if not ans or lst[i + 1] - lst[i] - 1 > ans[1] - ans[0] + 1:
            ans = [lst[i] + 1, lst[i + 1] - 1]
    print(*ans)
