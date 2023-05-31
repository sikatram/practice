class Stack:
    def __init__(self):
        #set equal to [] not None
        self.stack = []

    # Can be done in one line
    def is_empty(self):
        return len(self.stack) == 0
    
    #Don't forget the size
    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.stack[-1]
            del self.stack[-1]
            return item
        
        else:
            raise Exception("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
        else:
            raise Exception("Stack is empty")