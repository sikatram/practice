from stack import Stack

def main():
    my_stack = Stack()

    my_stack.push("Node_1")
    my_stack.push("Node_2")
    my_stack.push("Node_3")

    my_stack.print_stack()

    print(my_stack.peek())
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(my_stack.peek())


if __name__ == "__main__":
    main()