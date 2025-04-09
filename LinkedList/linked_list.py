class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.add(40)
ll.append(80)
ll.add(30)
ll.append(70)
ll.add(20)
ll.append(60)
ll.add(10)
ll.append(50)
ll.display()