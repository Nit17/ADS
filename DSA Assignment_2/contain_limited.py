class SimpleQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return len(self.queue) == self.capacity
    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Queue is full. Cannot enqueue more items.")
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    def size(self):
        return len(self.queue)

my_queue = SimpleQueue(3)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.enqueue(4)

print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())

print("Peek:", my_queue.peek())

print("Size:", my_queue.size())
