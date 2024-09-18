class QueueError(IndexError):  # Choose IndexError as the base class for the new exception
    pass


class Queue:
    def __init__(self):
        self.__queue = []  # Initialize an empty list to store the queue elements

    def put(self, elem):
        self.__queue.insert(0, elem)  # Insert element at the beginning of the list

    def get(self):
        if len(self.__queue) == 0:  # Check if the queue is empty
            raise QueueError  # Raise custom QueueError if the queue is empty
        return self.__queue.pop()  # Remove and return the last element


# Testing the Queue class
que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
