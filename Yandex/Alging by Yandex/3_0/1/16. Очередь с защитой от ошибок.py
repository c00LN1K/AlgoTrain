class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


class Queue:
    def __init__(self):
        self.length = 0
        self.head = self.tail = None

    def push(self, n):
        if self.tail is None:
            self.head = self.tail = Node(n)
        else:
            self.tail.next = Node(n)
            self.tail = self.tail.next
        self.length += 1
        return 'ok'

    def pop(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return node.val
        return 'error'

    def front(self):
        if self.head:
            return self.head.val
        return 'error'

    def size(self):
        return self.length

    def clear(self):
        self.head = self.tail = None
        self.length = 0
        return 'ok'

    def exit(self):
        return 'bye'


queue = Queue()
while k := input():
    if 'push' in k:
        print(queue.push(int(k.split()[-1])))
    elif 'pop' == k:
        print(queue.pop())
    elif 'size' == k:
        print(queue.size())
    elif 'clear' == k:
        print(queue.clear())
    elif 'front' == k:
        print(queue.front())
    elif 'exit' == k:
        print(queue.exit())
        break
