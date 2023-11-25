class maxheap:
    def __init__(self):
        self.heap = []
    
    def parent(self,i):
        return (i-1) // 2
    
    def lchild(self,i):
        return (2*i) + 1
    
    def rchild(self,i):
        return (2*i) + 2
    
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)] , self.heap[i]
            i = self.parent(i)
            
    def delete_max(self):
        if self.heap is None:
            print("None")
            return
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            max = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return max
        
    def heapify_down(self,i):
        largest = i
        left = self.lchild(i)
        right = self.rchild(i)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i] , self.heap[largest] = self.heap[largest] , self.heap[i]
            self.heapify_down(largest)
            
    def merge(self, other):
        new_heap = maxheap()
        new_heap.heap = (self.heap+other.heap)
        new_heap.heapify_up(len(new_heap.heap)-1)
        return new_heap
    
    def sort(self):
        sort_list = []
        while self.heap:
            sort_list.append(self.delete_max())
        return sort_list
    
    def print_heap(self):
        print(self.heap)
    
heap1 = maxheap()
heap1.insert(10)
heap1.insert(80)
heap1.insert(78)
heap1.insert(89)
heap1.insert(101)
heap1.insert(6)
heap1.insert(56)
heap1.insert(33)
print(heap1.rchild(1))
heap1.print_heap()
heap1.delete_max()
heap1.print_heap()

heap2 = maxheap()
heap2.insert(12)
heap2.insert(11)
heap2.insert(36)
heap2.insert(72)
heap2.insert(52)
merged_heap = heap1.merge(heap2)
print(merged_heap.heap)

sortedlist = merged_heap.sort()
print(sortedlist)


