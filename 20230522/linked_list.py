class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# data=None is a parameter with a default value. It means that this parameter is optional.

class LinkedList:

    # head is set to none and will be added to once data is inserted
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)

        # Don't forget the else statement
        else:
            current_node = self.head

            while current_node:
                current_node.next = Node(data)
                current_node = current_node.next


    def insert_at_beginning(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def insert(self, key):
        while current_node and current_node.data != 


    def print_linked_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse(self):
        if not self.head:
            return None
        
        previous_node = None
        current_node = self.head

        while current_node.next:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        current_node.next = previous_node


