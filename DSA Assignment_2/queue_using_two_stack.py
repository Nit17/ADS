class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operation
        self.stack2 = []  # Stack for dequeue operation

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        # Push elements onto stack1 for enqueue operation
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            return None  # Queue is empty

        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop and return the top element from stack2 (simulating dequeue operation)
        return self.stack2.pop()

# Create a queue using two stacks
my_queue = QueueUsingStacks()

# Enqueue elements into the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Dequeue elements from the queue
print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())

# Enqueue more elements
my_queue.enqueue(4)
my_queue.enqueue(5)

# Check if the queue is empty
print("Is Empty:", my_queue.is_empty())
