class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_Empty():
            return self.stack.pop()
        else:
           print("Stack is Empty!!!")
        
    def is_Empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        if not self.is_Empty():
            return self.stack[-1]
        else:
           print("Stack is Empty!!!")
        
    def print_stack(self):
        if not self.is_Empty():
            print(self.stack)
        else:
            print("Stack is Empty!!!")
    
stack1 = stack()
stack1.push(2)
stack1.push(5)
stack1.push(10)
stack2 = stack()
stack1.pop()
stack1.print_stack()
