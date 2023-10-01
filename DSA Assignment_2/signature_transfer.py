class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def transfer(S, T):
    while not S.is_empty():
        item = S.pop()
        T.push(item)

# Test the transfer function
S = Stack()
T = Stack()

S.push(1)
S.push(2)
S.push(3)

print("Stack S before transfer:", S.items)
print("Stack T before transfer:", T.items)

transfer(S, T)

print("Stack S after transfer:", S.items)
print("Stack T after transfer:", T.items)
