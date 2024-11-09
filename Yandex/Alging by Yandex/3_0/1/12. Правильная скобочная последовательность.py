def solve():
    stack = []
    d = {')': '(', '}': '{', ']': '['}
    for el in s:
        if el in d and stack and stack[-1] == d[el]:
            stack.pop()
        elif el not in d:
            stack.append(el)
        else:
            return False
    return len(stack) == 0


s = input()
print('yes' if solve() else 'no')
