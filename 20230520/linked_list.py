def hello_world():
    print("Hello from another file!")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #O(n)
    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    #O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #O(n)
    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        
        previous_node.next = current_node.next
        current_node = None
    
    #O(n)
    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

