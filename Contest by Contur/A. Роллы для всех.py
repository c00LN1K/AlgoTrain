n, t = map(int, input().split())
s1 = sum(map(int, input().split()))
s2 = sum(map(int, input().split()))

if t < s1 or t > s2:
    print("NO")
else:
    print("YES")
