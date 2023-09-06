class Stack:

    def __init__(self):

        self.items = []

 

    def is_empty(self):

        return len(self.items) == 0

 

    def is_full(self):

        if stack_size is not None:

            return len(self.items) == stack_size

        return False

 

    def push(self, item):

        if not self.is_full():

            self.items.append(item)

        else:

            

            print("Stack is full")

            

 

    def pop(self):

        if not self.is_empty():

            return self.items.pop()

        else:

            print("Stack is empty") #IndexError("Stack is empty")

 

    def peek(self):

        if not self.is_empty():

            return self.items[-1]

        else:

            print("Stack is empty")#print IndexError("Stack is empty")

 

    def size(self):

        return len(self.items)

 

stack_size=3  # If we need limited stack size declare the size or else just declare as None like this stack_size=None

stack = Stack() #creating the object of the class

 

stack.push(1)#Pushing the element to stack

stack.push(2)

stack.push(3)

stack.push(4)

 

print("Stack size:", stack.size())  

print("Top element:", stack.peek())  

 

 

print(stack.pop())