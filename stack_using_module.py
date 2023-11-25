import collections
stack = collections.deque()
import queue
stack = queue.LifoQueue()
def push():
    element = int(input("Enter The Element:"))
    stack.put(element)
    print(stack)
def pop():
    if not stack:
        print("Stack Is Empty")
    else:
        e = stack.get(timeout=1)
        print(f"Removed The Element {e}")
        print(stack)
def stack_top():
    if not stack:
        print("The Stack Is Empty!")
        return
    top = stack[-1]
    print(top)
while True:
    print("____Select The Operation____\n1.Push \n2.Pop \n3.Stack Top \n4.Quit")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        stack_top()   
    elif choice == 4:
        break
    else:
        print("Enter Correct Operation!!")