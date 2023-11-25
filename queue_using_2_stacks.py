class QueueUsingStacks:
    def __init__(self):
        self.stack1 =[]
        self.stack2 = []
    
    def enqueue(self,item):
        
        #push all elements from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(item)
        
        #push back all elements from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack1.pop())
        
    def dequeue(self):
        #if both stacks are empty the queue is empty
        
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
        else:
            return self.stack1.pop()
         
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1)
    
    
queue1 =  QueueUsingStacks()
queue1.dequeue()