from queue import Queue
from stack import Stack

def main():
    my_stack = Stack()
    my_stack.push("Hello")
    my_stack.push("World")
    my_stack.push("Yes")
    print(my_stack.display())
    my_stack.pop()
    print(my_stack.display())

if __name__ == "__main__":
    main()