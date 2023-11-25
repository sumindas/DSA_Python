class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_List:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head == None:
            print("Linked List Is Empty!!!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref
    def add_Begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_End(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_After(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("The Node Not Present in Linked List!!!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_Before(self,data,x):
        if self.head is None:
            print("Linked List Is Empty!!!")
            return
        if self.head.data == x: 
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("The Node Not Present In Linked List!!!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node       
    def insert_Empty(self,data):
        if self.head is not None:
            print("Linked List is Not Empty!!!")
        else:
            new_node = Node(data)
            self.head = new_node
    def delete_Begin(self):
        if self.head is None:
            print("Delete Not Possible Because Linked List Is Empty!!")
        else:
            self.head = self.head.ref       
    def delete_End(self):
        if self.head is None:
            print("Delete Not Possible Because Linked List Is Empty!!")
            return
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_Any_by_Value(self,x):
        if self.head is None:
            print("Delete Not Possible Because Linked List Is Empty!!")
            return
        if self.head.data == x:
            self.head = self.head.ref
        
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("\nNode Note Present in Linked List!!!")
        else:
            n.ref = n.ref.ref            
    def linkedlist_To_array(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.data)
            current = current.ref  
        array.sort()  
        return array
    
    def array_To_Linked_List(self,array):
        if not array:
            return None
        self.head = Node(array[0])
        n = self.head
        for i in range(1,len(array)):
            new_node = Node(array[i])
            n.ref = new_node
            n = new_node
        
        arraylink = self.head
        while arraylink is not None:
            print(arraylink.data,"->",end=" ")
            arraylink = arraylink.ref
        
    def reverse_LL(self):
        current_node = self.head
        next_node = self.head
        prvious_node = None
        while current_node is not None:
            next_node = next_node.ref
            current_node.ref = prvious_node
            prvious_node = current_node
            current_node = next_node
        self.head = prvious_node
        
    def reverse_recursion(self,n):
        if n is None:
            return
        self.reverse_recursion(n.ref)
        print(n.data,"->",end=" ")
        
    def merge_linked_list(self):
        ll3 = Linked_List()
        self.ll2 = ll2
        self.ll3 = ll3
        n = ll2.head
        while n.ref is not None:
            n = n.ref
        n.ref = ll3.head
        
        
            
                
            
          
                                     
LL1 = Linked_List()
# LL1.add_End(90)
# LL1.add_Begin(100)
# LL1.add_Begin(12)
# LL1.add_End(70)
# LL1.add_Begin(78)
# LL1.add_Before(35,300)
# LL1.add_Before(567,355)
# LL1.insert_Empty(12)
# LL1.add_After(300,12)
# LL1.add_Begin(100)
# LL1.add_Begin(102)
# LL1.add_Begin(678)
# LL1.add_Begin(62)
# LL1.add_Begin(78)
ll2 = Linked_List()
# ll2.add_End(10)
# ll2.add_End(20)
# ll2.add_End(30)
# ll2.add_End(40)
# ll2.delete_Any_by_Value(40)
# ll2.print_LL()
# ll3 = Linked_List()
# ll3.add_End(50)
# ll3.add_End(60)
# ll3.add_End(70)
# ll3.add_End(80)
# ll2.add_Before(90,10)
# ll2.print_LL()
# print()
# ll3.print_LL()
# ll2.print_LL()
# LL1.print_LL()
# LL1.delete_Any_by_Value(100)
# print("\nLinked List After Deletion")
# LL1.print_LL()
# print()
# arraylink = LL1.linkedlist_To_array()
# print(arraylink)
linkarray = LL1.array_To_Linked_List([1,2,3,4,5])
# print()
# LL1.reverse_LL()
# LL1.print_LL()
# print()
# LL1.reverse_recursion(LL1.head)
print(LL1.linkedlist_To_array())
