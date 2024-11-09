def solve():
    s = int(input())
    lst1 = list(map(int, input().split()))[1:]
    lst2 = list(map(int, input().split()))[1:]
    d = {}
    for i, el in enumerate(list(map(int, input().split()))[1:]):
        if el not in d:
            d[el] = i
    
    for i, el1 in enumerate(lst1):
        if el1 > s:
            continue
        for j, el2 in enumerate(lst2):
            if (el1 + el2) > s:
                continue
            dif = s - el1 - el2
            if dif in d:
                return i, j, d[dif]

res = solve()
print(*res if res else [-1])

