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
        if self.size()  > 0:
            return self.queue.pop(0)
        else:
            return None
        
    def display(self):
        return self.queue