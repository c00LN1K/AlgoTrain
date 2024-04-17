ans = set()
lst = []

for i in range(3):
    n = int(input())
    lst.append(set(map(int, input().split())))

print(*sorted(lst[0] & lst[1] | lst[1] & lst[2] | lst[0] & lst[2]))
