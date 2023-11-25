class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
                
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                 print("Node is Not Found")
                 
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                 print("Node is Not Found")
                 
    def preorder(self):
        
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
    def inorder(self):
        
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
        
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ") 
    
    def delete(self,data,current):
        if self.key is None:
            print("The Tree Is Empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,current)
            else:
                print("The Node Is Note Present")
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("The Node Is Note Present")
                
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return self 
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return self
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,current)
        return self

    def min_node(self):
        current = self.key
        while current.lchild:
            current = current.lchild
        print("Node With Smallest Key is:",current.key)
        
    def max_node(self):
        current = self.key
        while current.rchild:
            current = current.rchild
        print("Node With Smallest Key is:",current.key)
        
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)    
    
    
                     
                 
                 
key = BST(10)
list1 = [12,76,98,90,76,45,3,2]
for i in list1:
        key.insert(i)
key.search(10)
key.min_node()
print("Preorder")
key.preorder()
print("\nInorder")
key.inorder()
print("\nPostorder")
key.postorder()
print("\nNo of Nodes:",count(key))
if count(key) >= 1:
    key.delete(10,key.key)
else:
    print("Cannot Delete !!!")
