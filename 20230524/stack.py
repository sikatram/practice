class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        
        else:
            return None

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        
        else:
            return None

    def display(self):
        return self.stack