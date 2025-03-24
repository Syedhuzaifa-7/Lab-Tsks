from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if self.is_empty():
            return None 
        return self.elements.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0]

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.elements) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.elements)

my_queue = Queue()


my_queue.enqueue(30)
print("Queue size:", my_queue.size())
print("Is empty:", my_queue.is_empty())

print("Dequeued:", my_queue.dequeue())