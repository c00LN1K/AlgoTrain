n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [-1] * n

for i in range(n):
    while stack and stack[-1][0] > lst[i]:
        _, index = stack.pop()
        ans[index] = i
    stack.append((lst[i], i))

print(*ans)
