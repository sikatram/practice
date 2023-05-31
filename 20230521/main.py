from linked_list import LinkedList
from stack import Stack

def main():
    stack_practice()

def linked_list_practice():
    list = ["Node_1", "Node_2", "Node_3"]

    ll = LinkedList()
    
    for x in list:
        ll.insert_at_end(x)

    ll.insert_at_beginning("Node_0")

    ll.reverse_linked_list()

    ll.print_list()

def stack_practice():
    items = ["item_1", "item_2", "item_3"]

    stack = Stack()

    for x in items:
        stack.push(x)

    print(stack.size())

    stack.pop()

    print(stack.size())


if __name__ == "__main__":
    main()