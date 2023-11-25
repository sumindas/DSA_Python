class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # If the slot is already occupied, find the next available slot
        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)

        # Search for the key in the hash table
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)

        # Search for the key in the hash table
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

        raise KeyError("Key not found")



hash_table = HashTable(10)  

hash_table.insert(3, "Value 1")
hash_table.insert(13, "Value 2")
hash_table.insert(23, "Value 3")

print(hash_table.search(3))  
print(hash_table.search(13))  
print(hash_table.search(23))  

hash_table.delete(13)

print(hash_table.search(13))  
