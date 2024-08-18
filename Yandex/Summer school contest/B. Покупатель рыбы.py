from collections import deque

n, k = map(int, input().split())
ans = [0] * n
prices = list(map(int, input().split()))
stack = deque()
for i in range(n):
    while stack and (i - stack[0]) >= k:
        stack.popleft()
    while stack and ((i - stack[-1]) >= k or prices[stack[-1]] >= prices[i]):
        stack.pop()
    stack.append(i)
    ans[stack[0]] += 1

print(sum(num * price for price, num in zip(prices, ans)))
print(*ans)
