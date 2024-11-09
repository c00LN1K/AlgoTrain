from collections import deque

n, k = map(int, input().split())
lst = list(map(int, input().split()))

stack = deque()
deleted = set()

for i in range(k):
    while stack and stack[-1][0] > lst[i]:
        stack.pop()
    stack.append((lst[i], i))

ans = [0] * (n - k + 1)
ans[0] = stack[0][0]

for i in range(k, n):
    deleted.add(i - k)
    while stack and stack[0][1] in deleted:
        stack.popleft()
    while stack and stack[-1][0] > lst[i]:
        stack.pop()
    stack.append((lst[i], i))
    ans[i - k + 1] = stack[0][0]

print(*ans, sep='\n')
