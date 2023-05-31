#Don't forget about instances where the stack may be empty

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None

        else:
            item = self.stack[-1]
            del self.stack[-1]
            return item
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    
    def display(self):
        return self.stack