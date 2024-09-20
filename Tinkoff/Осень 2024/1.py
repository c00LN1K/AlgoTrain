lst = input().split(',')

ans = []
for el in lst:
    if '-' in el:
        l, r = el.split('-')
        ans.extend([val for val in range(int(l), int(r) + 1)])
    else:
        ans.append(el)

print(*ans)