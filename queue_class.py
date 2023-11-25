class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,item):
        self.queue.append(item)
    
    def dqueue(self):
        if not self.is_Empty():
            return self.queue.pop(0)
        else:
            print("The Queue is Empty!!!")
    
    def is_Empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        if  not self.is_Empty():
            print(self.queue[0])
        else:
            print("The Queue is Empty!!!")
    
    def rear(self):
        if  not self.is_Empty():
            print(self.queue[len(self.queue)-1])
        else:
            print("The Queue is Empty!!!")
    
    def print_queue(self):
        if not self.is_Empty():
            print(self.queue)
        else:
            print("The Queue is Empty!!!")
    
            
            
    
    
queue1 = Queue()
queue1.enqueue(10)
queue1.enqueue(11)
queue1.print_queue()
queue1.enqueue(20)
queue1.dqueue()
queue1.dqueue()
queue1.dqueue()
queue1.dqueue()
queue1.print_queue()

queue1.front()
queue1.rear()