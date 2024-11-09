def solve():
    s = input()
    stack = 0
    for el in s:
        if el == '(':
            stack += 1
        elif el == ')':
            if not stack:
                return 'NO'
            stack -= 1
    if stack:
        return 'NO'
    return 'YES'
print(solve())