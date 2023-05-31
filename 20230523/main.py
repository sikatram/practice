from queue import Queue

def main():
    q = Queue()
    print(q.is_empty())  # True
    q.enqueue('Apple')
    q.enqueue('Banana')
    q.enqueue('Cherry')
    print(q.display())  # ['Apple', 'Banana', 'Cherry']
    print(q.size())  # 3
    print(q.dequeue())  # 'Apple'
    print(q.display())  # ['Banana', 'Cherry']
    print(q.is_empty())  # False


if __name__  == "__main__":
    main()