from linked_list import LinkedList

ll = LinkedList()

while True:
    print("Options: ")
    print("1. Add at end")
    print("2. Add at beginning")
    print("3. Display")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("0. Exit")
    
    choice = int(input("Enter you choice: "))
    
    choice_list = [0,1,2,3,4,5]
    if choice not in choice_list:
        print("invalid choice")
        break

    if choice == 1:
        data = int(input("Enter the data : "))
        ll.append(data)

    if choice == 2:
        data = int(input("Enter the data : "))
        ll.add(data)

    if choice == 3:
        print("The data in linked list : ")
        ll.display()

    if choice == 4:
        ll.delete_beginning()

    if choice == 5:
        ll.delete_end()

    if choice == 0:
        print("Exit")
        break