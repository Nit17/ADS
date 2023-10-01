class unlimited_SizeStack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
            return None
    def peek (self):
        if not self.is_empty():
            return None
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    
#Example stack

stack=unlimited_SizeStack()

stack.push(1)
stack.push(2)
stack.push(3)

print("stack size:",stack.size())
print("Top element:",stack.size())

while not stack.is_empty():
    print("popper:",stack.pop())
print("stack size:",stack.size())
