class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Simple hash function that calculates the index based on the key's ASCII values
        total = sum(ord(char) for char in key)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        node = Node(key, value)

        # If the bucket is empty, create a new node and add it
        if self.table[index] is None:
            self.table[index] = node
        else:
            # If there are existing nodes in the bucket, append the new node at the end
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = node

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        # Traverse the linked list in the bucket to find the node with the matching key
        while current:
            if current.key == key:
                return current.value
            current = current.next

        # If the key is not found, return None
        return None

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None

        # Traverse the linked list in the bucket to find the node with the matching key
        while current:
            if current.key == key:
                # If the node is the first node in the bucket
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return

            previous = current
            current = current.next

    def display(self):
        for index, bucket in enumerate(self.table):
            current = bucket
            print(f"Bucket {index}:", end=" ")

            while current:
                print(f"{current.key}:{current.value}", end=" -> ")
                current = current.next

            print("None")


# Example usage:
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 8)
hash_table.insert("cat", 3)
hash_table.insert("dog", 2)
hash_table.insert("urumi",2)
hash_table.insert("elephant", 9)

hash_table.display()


print(hash_table.get("cat"))  # Output: 3
print(hash_table.get("elephant"))  # Output: 9

hash_table.remove("banana")
hash_table.display()

