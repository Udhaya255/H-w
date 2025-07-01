stack = []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty.")
        return None
    else:
        popped = stack.pop()
        return popped

def display(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("--- Stack Contents ---") 
        for item in reversed(stack): 
            print(item)
        print("") 

running = True
while running:
    print("\n+--------------------+")
    print("|    Operations      |")
    print("+--------------------+")
    print("| 1. Push item       |")
    print("| 2. Pop item        |")
    print("| 3. Display stack   |")
    print("| 4. Exit            |")
    print("+--------------------+")
    
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        
        print("Enter items to push (type -99 to stop):")
        while True:
            item_to_push = input("Item to push: ")
            if item_to_push == '-99':
                break
            push(stack, item_to_push)
    elif choice == '2':
        popped = pop(stack)
        if popped is not None:
            print(f"'{popped}' popped.") 
    elif choice == '3':
        display(stack)
    elif choice == '4':
        print("Exiting.")
        running = False
    else:
        print("Invalid choice.")
