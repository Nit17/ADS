class limitedSizeStack:
    def __init__(self,limit):
        self.limit=limit
        self.stack=[]
    def push(self,item):
        if len(self.stack)<self.limit:
            self.stack.append(item)
        else:
            print("stack is full.Cannot push item:",item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("stack is empty")
            return None
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    
#Example Usage 

stack = limitedSizeStack(5)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("stack size:",stack.size())
stack.push(6)
print("Top elemnt:",stack.peek())
while not stack.is_empty():
    print("popped:",stack.pop())
print("stack size:",stack.size())
