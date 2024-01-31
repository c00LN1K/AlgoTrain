k = int(input())

for _ in range(k):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    p1 = p2 = 0

    for i in range(1, n + 1):
        p1 += abs(lst1[i - 1] - i)
        p2 += abs(lst2[i - 1] - i)
    print(p1, p2)

