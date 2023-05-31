class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def remove(self, data):
        previous_node = None
        current_node = self.head

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node.data == data:
            previous_node.next = current_node.next
            del current_node

    def reverse(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node