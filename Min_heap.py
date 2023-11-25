class minheap:
    def __init__(self):
        self.heap = []
    
    def parent(self,i):
        return (i-1) // 2
    
    def lchild(self,i):
        return (2*i) + 1
    
    def rchild(self,i):
        return (2*1) + 2
    
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self,i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)] , self.heap[i]
            i = self.parent(i)
            
    def heap_down(self,i):
        smallest = i
        left = self.lchild(i)
        right = self.rchild(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != i:
            self.heap[i] , self.heap[smallest] = self.heap[smallest] , self.heap[i]
            self.heap_down(smallest)
            
heap1 = minheap()
heap1.insert(100)
heap1.insert(200)
heap1.insert(3)
heap1.insert(4)
heap1.insert(5)
heap1.insert(60)
heap1.insert(90)
print(heap1.heap)