class Hash_Table:
    def __init__(self,size):
        self.size = size
        self.table = [[]for x in range(size)]
    
    def _hash_function(self,key):
       return hash(key) % self.size
    
    def add(self,key,value):
        index = self._hash_function(key)
        bucket = self.table[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket [i] = (key,value)
                return
        bucket.append((key,value))
        
    def get(self,key):
        index = self._hash_function(key)
        bucket = self.table[index]
        
        for k,v in bucket:
            if k == key:
                return v
            raise KeyError(f"key {key} not found")
        
    def remove(self,key):
        index = self._hash_function(key)
        bucket = self.table[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"key {key} not found")
    
    def print_hashtable(self):
        for bucket in self.table:
            for key,value in bucket:
                print(f"key: {key}, value: {value}")
                
            


HH1 = Hash_Table(10)
HH1.add("apple",7)
HH1.add("orange",9)
HH1.add("munthiri",10)
print(HH1.get("apple"))
HH1.add("orange",9)
print(HH1._hash_function("apple"))
HH1.print_hashtable()