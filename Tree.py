class GeneralTree:
    def __init__(self, key):
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
   
   
tree = GeneralTree(10)
tree.insert(10)
tree.insert(7)
tree.insert(18)
tree.insert(76)
tree.insert(70)
tree.print_tree()

tree.delete_primes()
print()


