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
        while self.head.next:
            self.head = self.head.next
        self.head = None
        print(self.head.data)


    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")