class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)  

s1= Stack()
s1.push(10)
s2= Stack()
s2.push(20) 
s3= Stack()
s3.push(30)   

print(s1.pop()) 
print(s1.pop())  
print(s2.pop()) 
print(s3.pop()) 