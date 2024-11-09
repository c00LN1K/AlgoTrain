n = int(input())
lst = list(map(int, input().split()))

prefix1 = [0] * (n + 1)
for i in range(n, 0, -1):
    prefix1[i - 1] = prefix1[i] + lst[i - 1]

lst2 = []
for j in range(n - 1):
    lst2.append(lst[j] * prefix1[j + 1])

prefix2 = [0] * (len(lst2) + 1)
for i in range(len(lst2), 0, -1):
    prefix2[i - 1] = prefix2[i] + lst2[i - 1]

ans = []
for i in range(n - 2):
    ans.append(lst[i] * prefix2[i + 1])

print(sum(ans) % 1_000_000_007)
