class Stack():
    def __init__(self):
        self.stack = []

    #O(1)
    def is_empty(self):
        return len(self.stack) == 0
    
    #O(1)
    def push(self, item):
        self.stack.append(item)

    #O(1)
    def pop(self):
        if not self.is_empty():
            item = self.stack[-1]
            del self.stack[-1]
            return item

        else:
            raise Exception("Stack is empty")
        
    #O(1)
    def peep(self):
        if not self.is_empty():
            return(self.stack[-1])
        else:
            raise Exception("Stack is empty")
    
    #O(1)
    def size(self):
        return len(self.stack)
    
    #O(n)
    def print_stack(self):
        for item in self.stack:
            print(item)