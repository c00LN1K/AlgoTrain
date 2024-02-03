n = int(input())
stack = list(map(int, input().split()))

for i in range(n - 1, -1, -1):
    try:
        if stack[i] % 2 == 0:
            print(stack[i])
            break
    except Exception:
        pass
else:
    print(-1)
