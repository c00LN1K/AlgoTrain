n = int(input())
stack = []
prefix = [0]

for _ in range(n):
    k = input()
    if k[0] == '+':
        num = int(k[1:])
        stack.append(num)
        prefix.append(prefix[-1] + num)
    elif k[0] == '-':
        print(stack.pop())
        prefix.pop()
    elif k[0] == '?':
        print(prefix[-1] - prefix[-int(k[1:]) - 1])
