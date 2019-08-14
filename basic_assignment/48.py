class LIFOQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(-1)
        else:
            raise Exception("Your queue is empty")


my_queue = LIFOQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

first = my_queue.dequeue()
second = my_queue.dequeue()
third = my_queue.dequeue()

print("First: " + str(first))
print("Second: " + str(second))
print("Third: " + str(third))
