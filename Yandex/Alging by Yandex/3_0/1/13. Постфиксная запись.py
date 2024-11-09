s = input().split()
stack = []
for el in s:
    if el.isdigit():
        stack.append(int(el))
    elif el == '+':
        first, second = stack.pop(), stack.pop()
        stack.append(first + second)
    elif el == '-':
        first, second = stack.pop(), stack.pop()
        stack.append(second - first)
    elif el == '*':
        first, second = stack.pop(), stack.pop()
        stack.append(first * second)
print(stack[0])
