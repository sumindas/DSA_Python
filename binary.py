class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(data,self.root)
    
    def insert_recursive(self,data,current):
        if current.left is None:
            current.left = Node(data)
        else:
            self.insert_recursive(data,current.left)
        if current.right is None:
            current.right = Node(data)
        else:
            self.insert_recursive(data,current.right)
            
    def print_tree(self):
        if self.root is None:
            print("Tree Is Empty")
        else:
            self.print_tree_recursive(self.root)
        
    def print_tree_recursive(self,current):
        if current is not None:
            print(current.data)
            if current.left:
                self.print_tree_recursive(current.left)
            elif current.right:
                self.print_tree_recursive(current.right)
            else:
                return
            
    def search(self,data):
        if self.root == data:
            return self.root
        else:
            return self.search_recursive(self.root,data)
    
    def search_recursive(self,current,data):

        if current.left:
            return self.search_recursive(current.left,data)
        elif current.right:
            return self.search_recursive(current.right,data)
        

        
        



tree1 = BinaryTree()
tree1.insert(10)
tree1.insert(20)
tree1.insert(30)
tree1.insert(40)
tree1.print_tree()
search =  tree1.search(10)
print(search)

if search is not None:
    print("Value Found")
else:
    print("Value Not Found")