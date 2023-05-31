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
            self.head =  Node(data)
            #You don't have to return the head. We're just modifying the list.
            # return self.head
        
        #Since you are not returning anything, you need an else block
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
                current_node.next = Node(data)

    #O(1)
    def insert_at_beginning(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    #O(n)
    def delete_node(self, key):
        current_node = self.head

        # Must check is current_node exists
        # Don't forget to return after this
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None

        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node == None:
            return
            
        previous_node.next = current_node.next
        current_node = None

    def reverse_linked_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def print_list(self):
        current_node = self.head

        #go to next node
        while current_node:
            print(current_node.data)
            current_node = current_node.next