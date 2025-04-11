from node import Node

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def add(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node


    def delete_beginning(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return 
        self.head = self.head.next
    

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    def add_at_position(self, data: int, position: int):
        new_node = Node(data)
        temp = self.head
        temp2 = temp
        for i in range(1, position):
            temp2 = temp
            temp = temp.next
        
        new_node.next = temp2.next
        temp2.next = new_node

        
    def search_by_value(self, data:int):
        k = False
        index = 0
        temp = self.head
        while temp.next:
            if temp.data == data:
                k = True
                break
            else:
                k = False
            temp = temp.next
            index += 1

        if k == True:
            return f"{data} is available in list at index {index}"
        else:
            return f"{data} is not available in list"


    def search_by_index(self, index: int):
        if index >= self.count(self):
            return f"Invalid index"
        temp = self.head
        for i in range(0, index):
            temp = temp.next
        return f"{temp.data} is at index {index}"


    def display(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.data)
            else:
                print(temp.data, end=" -> ")
            temp = temp.next

    
    def count(self):
        total = 1
        temp = self.head
        while temp.next:
            total += 1
            temp = temp.next
        return total
    

    def reverse_list(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node  # Reverse the link
            previous_node = current_node
            current_node = next_node

        self.head = previous_node