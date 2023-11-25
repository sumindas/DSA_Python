class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def quadratic_probe(self, key, i):
        c1 = 1  # First constant for quadratic probing
        c2 = 1  # Second constant for quadratic probing
        return (self.hash(key) + c1 * i + c2 * (i ** 2)) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            i = 1
            while True:
                index = self.quadratic_probe(key, i)
                if self.table[index] is None:
                    self.table[index] = (key, value)
                    break
                i += 1

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        else:
            i = 1
            while True:
                index = self.quadratic_probe(key, i)
                if self.table[index] is not None and self.table[index][0] == key:
                    return self.table[index][1]
                i += 1
                if i >= self.size:
                    break
        return None

hashtable = HashTable(10)
hashtable.insert(5,"sumin")
hashtable.insert(15,"sumin")
hashtable.insert(25,"arjun")
hashtable.insert(35,"sahad")

print(hashtable.get(5))  
print(hashtable.get(15))  
print(hashtable.get(25))  
print(hashtable.get(35))  
print(hashtable.get(45)) 