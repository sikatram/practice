class Stack:

    def __init__(self):
        self.stack = []


    # Rememeber to consider the length of the stack
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.stack[-1]
            del self.stack[-1]

        else:
            raise Exception("Stack is empty")

        return item

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
        else:
            raise Exception("Stack is empty")
    
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        if not self.is_empty():
            for item in self.stack:
                print(item)

        else:
            raise Exception("Stack is empty")