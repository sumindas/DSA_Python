class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for x in range(self.max)]
    
    def get_hash(self,key):
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.max
    
    def add_to_hash(self,key,value):
        h = self.get_hash(key)
        self.arr[h].append((key,value)) 
        
    def display(self):
        data = [data for data in self.arr if len(data) > 0]
        print(data)
    
    def single_delete(self,key,value):
        h = self.get_hash(key)
        if len(self.arr[h]) > 0:
            for idx in range(len(self.arr[h])):
                if self.arr[h][idx][1] == value:
                   self.arr[h].pop(idx)
                   break
               
    def duplicate_delete(self,x):
        uni = set()
        dep = []
        
        for idx in range(self.max):
            if len(self.arr[idx]) > 0:
                for n_idx in range(len(self.arr[idx])):
                    key,value = self.arr[idx][n_idx]
                    if key == x:
                        if value not in uni:
                            uni.add(value)
                        else:
                            dep.append((idx,n_idx))
        
        for idx,n_idx in reversed(dep):
            self.arr[idx].pop(n_idx)
            
h1 = Hashtable()
h1.add_to_hash(1,"sumin")
h1.add_to_hash(1,"sumin")
h1.add_to_hash(1,"sumin")
h1.add_to_hash(2,"arjun")
h1.add_to_hash(3,"susmith")
h1.duplicate_delete(1)
h1.single_delete(1,"sumin")
h1.display()