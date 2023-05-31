class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    #Don't forget to pop at the zero index
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def display(self):
        print(self.queue)