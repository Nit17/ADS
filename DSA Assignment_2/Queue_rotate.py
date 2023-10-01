class QueueWithRotate:
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

    def rotate(self):
        if not self.is_empty():
            temp_stack = []
            
            # Pop elements from the queue and push them onto the temporary stack
            while not self.is_empty():
                temp_stack.append(self.dequeue())
            
            # Pop elements from the temporary stack and enqueue them back into the queue
            while temp_stack:
                self.enqueue(temp_stack.pop())

    def __str__(self):
        return str(self.queue)

# Create a queue with some elements
my_queue = QueueWithRotate()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

# Print the original queue
print("Original Queue:", my_queue)

# Rotate the queue to reverse the order of elements
my_queue.rotate()

# Print the rotated queue
print("Rotated Queue:", my_queue)
