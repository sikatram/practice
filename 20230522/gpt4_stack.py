class Stack:
    def __init__(self):
        self.stack = []

    # Method to add data to the stack
    # Add data to the top
    def push(self, data):
        self.stack.append(data)

    # Method to remove data from the stack
    # Remove data from the top
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to get the size of the stack
    def size(self):
        return len(self.stack)

    # Method to see the top of the stack without removing any elements
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack[-1]
