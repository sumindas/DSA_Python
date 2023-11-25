class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[]for x in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.max
    
    def second_hash(self,key):
        h = 7
        for char in str(key):
            h += ord(char)
        return h % self.max
    
    def add_hash(self,key,value):
        h = self.get_hash(key)
        idx = h
        n_idx = self.get_hash(key)
        count = 1
        while True:
            if len(self.arr[idx]) == 0:
                self.arr[idx].append((key,value))
                break
            idx = (idx + n_idx + count) % self.max
            count += 1
            
            if idx == h or count > self.max:
                 print("Hash Full")
                 return
            
    def single_delete(self,key,value):
        h = self.get_hash(key)
        idx = h
        n_idx = self.get_hash(key)
        count = 1
        while True:
            if len(self.arr[idx]) == 0:
                print("No data")
                return
            for item in self.arr[idx]:
                if item[1] == value:
                    self.arr[idx] = []
                    return
            idx = (idx + n_idx + count) % self.max
            count += 1
            if idx == h or count > self.max:
                print("No Hash")
                break
    def delete_dup(self):
        uni = set()
        dep = []
        for idx in range(self.max):
            if len(self.arr[idx]) > 0:
                for item in self.arr[idx]:
                    value = item[1]
                    if value not in uni:
                        uni.add(value)
                    else:
                        dep.append(idx)
                        
        for idx in dep:
            self.arr[idx].pop()
    
    def display(self):
        data = [ data for data in self.arr if len(data) > 0]
        print(data)
        
s1 = HashTable()
s1.add_hash(1,"sumin")
s1.add_hash(2,"sumindas")
s1.add_hash(1,"sumin")
s1.add_hash(3,"arjun")
s1.display()
s1.add_hash(4, "Shfa")
s1.add_hash(5, "Salman")
s1.display()
s1.single_delete(3, "hjkj")
s1.delete_dup()
s1.display()

                 
        