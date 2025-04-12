from linked_list import LinkedList

ll = LinkedList()

while True:
    print("")
    print("Options: ")
    print("1. Add at end")
    print("2. Add at beginning")
    print("3. Display")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Insert at Specific position")
    print("7. Search for an element")
    print("8. Search by index")
    print("9. count list")
    print("10. print reversed list")
    print("11. Detects if the linked list contains a cycle")
    print("12. Sort the linked list")
    print("13. Find the middle element")
    print("0. Exit")
    print("")
    
    choice = int(input("Enter you choice: "))
    
    choice_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
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

    if choice == 6:
        position = int(input("Enter the position : "))
        data = int(input("Enter the data : "))
        ll.add_at_position(data,position)

    if choice == 7:
        data = int(input("Enter the data to search : "))
        result = ll.search_by_value(data)
        print(result)
    
    if choice == 8:
        data = int(input("Enter index to search : "))
        result = ll.search_by_index(data)
        print(result)
    
    if choice == 9:
        print(f"The total elements in list is : {ll.count()}")

    if choice == 10:
        ll.reverse_list()

    if choice == 11:
        ll.detect_cycle()
    
    if choice == 12:
        ll.sort_list()
        
    if choice == 13:
        data = ll.middle_element()
        print(f"The the middle element is {data}")

    if choice == 0:
        print("Exit")
        break