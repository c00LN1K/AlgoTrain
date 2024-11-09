class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return self.val


class Queue:
    def __init__(self):
        self.length = 0
        self.head = self.tail = None

    def push_back(self, n):
        if self.tail is None:
            self.head = self.tail = Node(n)
        else:
            self.tail.next = Node(n, prev=self.tail)
            self.tail = self.tail.next
        self.length += 1
        return 'ok'

    def push_front(self, n):
        if self.head is None:
            self.head = self.tail = Node(n)
        else:
            self.head.prev = Node(n, next=self.head)
            self.head = self.head.prev
        self.length += 1
        return 'ok'

    def pop_front(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            self.length -= 1
            return node.val
        return 'error'

    def pop_back(self):
        if self.tail:
            node = self.tail
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            self.length -= 1
            return node.val
        return 'error'

    def front(self):
        if self.head:
            return self.head.val
        return 'error'

    def back(self):
        if self.tail:
            return self.tail.val
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
    if 'push_front' in k:
        print(queue.push_front(int(k.split()[-1])))
    elif 'push_back' in k:
        print(queue.push_back(int(k.split()[-1])))
    elif 'pop_front' == k:
        print(queue.pop_front())
    elif 'pop_back' == k:
        print(queue.pop_back())
    elif 'size' == k:
        print(queue.size())
    elif 'clear' == k:
        print(queue.clear())
    elif 'front' == k:
        print(queue.front())
    elif 'back' == k:
        print(queue.back())
    elif 'exit' == k:
        print(queue.exit())
        break
