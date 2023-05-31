from linked_list import LinkedList

def main():
    # Create a linked list
    ll = LinkedList()

    # Insert data at the end
    ll.insert_at_end("Node1")
    ll.insert_at_end("Node2")
    ll.insert_at_end("Node3")

    # Print the linked list
    print("Linked List after inserting at the end:")
    ll.print_list()

    # Insert data at the beginning
    ll.insert_at_beginning("Node0")

    # Print the linked list
    print("\nLinked List after inserting at the beginning:")
    ll.print_list()

    # Delete a node
    ll.delete_node("Node2")

    # Print the linked list
    print("\nLinked List after deleting a node:")
    ll.print_list()

if __name__ == "__main__":
    main()