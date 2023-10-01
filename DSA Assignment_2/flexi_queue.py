class FlexiQueue:
    def __init__(self, initial_capacity=5, expansion_factor=2, shrink_factor=0.5):
        self.queue = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity
        self.expansion_factor = expansion_factor
        self.shrink_factor = shrink_factor

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.size == self.capacity:
            self.expand()
        self.queue[self.size] = item
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue.pop(0)
            self.size -= 1
            if self.size < self.capacity * self.shrink_factor and self.capacity > 5:
                self.shrink()
            return item
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def expand(self):
        new_capacity = int(self.capacity * self.expansion_factor)
        self.queue += [None] * (new_capacity - self.capacity)
        self.capacity = new_capacity

    def shrink(self):
        new_capacity = max(int(self.capacity * self.shrink_factor), 5)
        self.queue = self.queue[:new_capacity]
        self.capacity = new_capacity

    def size(self):
        return self.size

# Create a FlexiQueue instance with an initial capacity of 5
my_queue = FlexiQueue()

# Enqueue elements
for i in range(1, 11):
    my_queue.enqueue(i)

# Dequeue elements
for i in range(5):
    print("Dequeue:", my_queue.dequeue())

# Shrink the queue's capacity
my_queue.dequeue()
my_queue.dequeue()

# Enqueue more elements
for i in range(11, 16):
    my_queue.enqueue(i)

# Peek at the front element
print("Peek:", my_queue.peek())

# Check the current size and capacity
print("Size:", my_queue.size())
print("Capacity:", my_queue.capacity)
