n = int(input())

_ = input()
ans = set(input().split())
for i in range(1, n):
    _ = input()
    ans &= set(input().split())

print(len(ans))
print(*sorted(ans))
