class StackUsingQueues:
    def __init__(self):
        self.queue1 = []  # Main queue representing the stack
        self.queue2 = []  # Temporary queue

    def is_empty(self):
        return len(self.queue1) == 0

    def push(self, item):
        # Pushing an element is done by enqueueing it to queue1
        self.queue1.append(item)

    def pop(self):
        if self.is_empty():
            return None  # Stack is empty

        # Move all elements from queue1 to queue2 except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        # Pop and return the last element from queue1 (simulating pop operation)
        item = self.queue1.pop(0)

        # Swap the queues (queue2 becomes the new main stack)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return item

    def top(self):
        if self.is_empty():
            return None  # Stack is empty

        # Move all elements from queue1 to queue2 except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        # Get and return the last element from queue1 (simulating top operation)
        item = self.queue1[0]

        # Move the last element to queue2
        self.queue2.append(self.queue1.pop(0))

        # Swap the queues (queue2 becomes the new main stack)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return item

# Create a stack using two queues
my_stack = StackUsingQueues()

# Push elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Pop elements from the stack
print("Pop:", my_stack.pop())
print("Pop:", my_stack.pop())

# Push more elements
my_stack.push(4)
my_stack.push(5)

# Get the top element
print("Top:", my_stack.top())
