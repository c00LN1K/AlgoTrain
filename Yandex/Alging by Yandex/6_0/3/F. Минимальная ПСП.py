n = int(input())
w = input()
s = input()
stack = []
for i in range(len(s)):
    if s[i] in {'[', '('}:
        stack.append(s[i])
    else:
        stack.pop()

print(stack)
