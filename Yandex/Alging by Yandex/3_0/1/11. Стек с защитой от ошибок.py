class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return 'ok'

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 'error'

    def size(self):
        return len(self.stack)

    def back(self):
        if self.stack:
            return self.stack[-1]
        return 'error'

    def clear(self):
        self.stack = []
        return 'ok'

    def exit(self):
        return 'bye'


stack = Stack()
while k := input():
    if 'push' in k:
        print(stack.push(k.split()[1]))

    elif k == 'pop':
        print(stack.pop())

    elif k == 'size':
        print(stack.size())

    elif k == 'back':
        print(stack.back())

    elif k == 'clear':
        print(stack.clear())

    elif k == 'exit':
        print(stack.exit())
        break
