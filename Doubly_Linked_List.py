class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
    def Forward_Traversal(self):
        if self.head is None:
            print("The Linked List Is Empty!!")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.nref
    def Bacwrad_Traversal(self):
        if self.head is None:
            print("The Linked List Is Empty!!")
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        print()
        while n is not None:
            print(n.data,"-->", end=" ")
            n = n.pref
    def insert_Empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List Is Not Empty")
    def insert_Begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    def insert_End(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    def insert_after(self,data,x):
        if self.head is None:
            print("The Linked List Is Empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("The Node Not Present in Linked List!!")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                     n.nref.pref = new_node
                n.nref = new_node
    def insert_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("The Node Not Present in Linked List!!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                
    def delete_Begin(self):
        if self.head is None:
            print("Deletion Not Possible Because Linked List Is Empty!!")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked list is Empty After The Node Is Deleted")
        else:
            self.head = self.head.nref
            self.head.pref = None
    def delete_End(self):
        if self.head is None:
            print("Delete Not Possible Because Linked List Is Empty!!")
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
    def delete_By_Value(self,x):
        if self.head is None:
            print("Delete Not Possible Because Linked List Is Empty!!")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("The Node is Not Present In Linked List")
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("The Node Is Not Present In Linked List!!")
                      
                                      
dd1 = Doubly_Linked_List()
dd1.insert_Begin(100)
dd1.insert_Begin(200)
dd1.insert_End(80)
dd1.insert_End(89)
dd1.insert_Begin(34)
dd1.insert_Begin(1000)
dd1.insert_after(67,100)
dd1.insert_before(99,1000)
dd1.Forward_Traversal()
print("\nAfter Delete")
dd1.delete_Begin()
dd1.delete_By_Value(100)
dd1.delete_By_Value(99)
dd1.Forward_Traversal()

# dd1.Forward_Traversal()
# dd1.Bacwrad_Traversal()

       