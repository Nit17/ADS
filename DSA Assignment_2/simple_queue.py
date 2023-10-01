class SimpleQueue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    def size(self):
        return len(self.queue)
my_queue = SimpleQueue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())
print("Peek:", my_queue.peek())

print("Size:", my_queue.size())
