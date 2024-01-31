n = int(input())

for i in range(n):
    c, a = map(int, input().split())
    print(c * (a // 2))
