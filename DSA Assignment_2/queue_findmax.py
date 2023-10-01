class QueueWithFindMax:
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

    def findMax(self):
        if not self.is_empty():
            max_value = self.queue[0]  # Initialize max_value with the first element

            # Dequeue and enqueue elements while keeping track of the maximum value
            for _ in range(len(self.queue)):
                item = self.dequeue()
                max_value = max(max_value, item)
                self.enqueue(item)

            return max_value
        else:
            return None

    def __str__(self):
        return str(self.queue)

# Create a queue with some elements
my_queue = QueueWithFindMax()
my_queue.enqueue(4)
my_queue.enqueue(8)
my_queue.enqueue(2)
my_queue.enqueue(10)
my_queue.enqueue(6)

# Print the original queue
print("Original Queue:", my_queue)

# Find the maximum value in the queue
max_value = my_queue.findMax()
print("Maximum Value:", max_value)

# Print the queue (unchanged)
print("Queue after findMax:", my_queue)
