def count_postfix(s):
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
    return stack[0]


def translate_to_postfix(s):
    # 1. Правильная скобочная последовательность
    # 2. Не может подряд идти две операции
    # 3. Не может начинаться и кончаться выражение или скобки на знак препинания (кроме отрицательных чисел, но они слитно с числом)
    # 4. Не может быть два числа подряд
    stack = []
    res = []
    for i in range(len(s)):
        pass
    return ''.join(res)


s = input()
