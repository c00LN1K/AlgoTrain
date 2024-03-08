n = int(input())
numbers = list(map(int, input().split()))

ans = ['+'] * (n - 1)
odds = []

for i in range(n):
    if numbers[i] % 2 == 1:
        odds.append(i)

if len(odds) % 2 == 0:
    ans[odds[0]] = 'x'
print(''.join(ans))
