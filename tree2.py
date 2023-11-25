class GeneralTree:
    def __init__(self, key) -> None:
        self.key = key
        self.children = []
    def insert(self, data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        else:
            new_child = GeneralTree(data)
            self.children.append(new_child)
           
    def search(self, data):
        if self.key is None:
            return False
        if self.key == data:
            if data == int:
                return True
        for i in self.children:
            if i.search(data):
                if data == int:
                 return True
        return False
   
   
    def print_tree(self):
        print(self.key, end=" ")
        for i in self.children:
            i.print_tree()
           
           
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n/2)):
            if n % i == 0:
                return False
        return True
   
    def delete_primes(self):
        if self.key is None:
            return

        self.children = [child for child in self.children if not child.is_prime(child.key)]

        return self.children
           
    def delete(self, data):
        if self.key is None:
            return
        if self.key == data:
            if self.children:
                new_root = self.children[0]
                self.key = new_root.key
                self.children = new_root.children
               
            else:
                self.key = None
            return

        for child in self.children:
            if child.key == data:
                self.children.remove(child)
                return
           
            child.delete(data)

        return
     
    
           
tree = GeneralTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(71)
tree.insert(2)
tree.search(2)

tree.print_tree()
if tree.search(10):
    print("Node found")
else:
    print("Node not found")

if tree.search(20):
    print("Node found")
else:
    print("Node not found")
   
tree.delete_primes()

tree.delete(10)
tree.print_tree()
