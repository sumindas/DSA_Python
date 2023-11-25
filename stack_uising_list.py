stack = []
def push():
    element = input("Enter The Element:")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("The Stack Is Empty!")
    else:
        e = stack.pop()
        print(f"Removed The Element {e}")
        print(stack)
def stack_top():
    if not stack:
        print("The Stack Is Empty!")
        return
    top = stack[-1]
    print(top)

def print_stack():
    print("Current Stack:", stack)
    
while True:
    print("____Select The Operation____\n1.Push \n2.Pop \n3.Stack Top \n4.Quit")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        stack_top()   
    elif choice == 4:
        print_stack()
    else:
        print("Enter Correct Operation!!")