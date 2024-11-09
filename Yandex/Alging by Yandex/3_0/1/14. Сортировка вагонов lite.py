def solve():
    stack = []
    curr = 1
    for carriage in carriages:
        stack.append(carriage)
        while stack and stack[-1] == curr:
            stack.pop()
            curr += 1
    return 'YES' if curr > n else 'NO'


n = int(input())
carriages = list(map(int, input().split()))
print(solve())
