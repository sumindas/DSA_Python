class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(data,self.root)
            
    def insert_recursive(self,data,node):
        if data < node.data:
            if node.lchild is None:
                node.lchild = Node(data)
            else:
                self.insert_recursive(data,node.lchild)
        else:
            if node.rchild is None:
                node.rchild = Node(data)
            else:
                self.insert_recursive(data,node.rchild)
        
    def search(self,data):
        return self.search_recursive(data,self.root)
    
    def search_recursive(self,data,node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search_recursive(data,node.lchild)
        else:
            return self.search_recursive(data,node.rchild)

    def delete(self,data):
        return self.delete_recursive(data,self.root)
    
    def delete_recursive(self,data,node):
        if node is None:
            return node
        if data < node.data:
            node.lchild = self.search_recursive(data,node.lchild)
        elif data > node.data:
            node.rchild = self.search_recursive(data,node.rchild)
        else:
            if node.lchild is None:
                return node.rchild
            elif node.rchild is None:
                return node.lchild
            min_node = self.min_node(node.rchild)
            node.rchild = self.delete_recursive(min_node.data,node.rchild)
        return node
    
    def min_node(self,node):
        current = node
        while current.left is not None:
            current = current.lchild
        return current

    def inorder_traverasal(self):
        self.inorder_recursive(self.root)
    
    def inorder_recursive(self,node):
        if node is not None:
            self.inorder_recursive(node.lchild)
            print(node.data, end=" ")
            self.inorder_recursive(node.rchild)
            
    def preorder_traverse(self):
        self.preorder_recursive(self.root)
        
    def preorder_recursive(self,node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_recursive(node.lchild)
            self.preorder_recursive(node.rchild)
            
    def postorder_traverse(self):
        self.postorder_recursive(self.root)
        
    def postorder_recursive(self,node):
        if node is not None:
            self.postorder_recursive(node.lchild)
            self.postorder_recursive(node.rchild)
            print(node.data, end=" ")
            
    def sorted_array_to_bst(self,array,start,end):
        if start > end:
            return 
        mid = start + end // 2
        self.insert(array[mid])
        self.sorted_array_to_bst(array,start,mid)
        self.sorted_array_to_bst(array,mid+1,end)
        
            
    
        
bst = BinarySearchTree()
bst.insert(8)
bst.insert(10)
bst.insert(109)
bst.insert(80)
bst.insert(60)
bst.insert(45)
bst.insert(17)
bst.insert(7)
bst.insert(78)
bst.insert(65)
bst.insert(1)
bst.insert(3)
bst.delete(109)
print("inorder")
bst.inorder_traverasal()
print()
print("postorder")
bst.postorder_traverse()
print()
print("preorder")
bst.preorder_traverse() 
array = [12,16,76,89,100,122]
bst.sorted_array_to_bst(array,0,len(array)-1)