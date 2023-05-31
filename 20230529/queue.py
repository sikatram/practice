#remember enqueue and dequeue

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            item = self.queue[0]
            del self.queue[0]
            return item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]
        
    def display(self):
        print(self.queue)