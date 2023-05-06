class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items.pop(0)

    def make_empty(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def make_new_queue(self, first_front, first_rear, second_front, second_rear, n):
        new_queue = Queue()
        if n == 1:
            new_queue.items = self.items[first_front:first_rear]
        elif n == 2:
            new_queue.items = self.items[second_front:second_rear]
        return new_queue

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.is_empty())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.is_empty())
    print(q)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.make_empty()

    print(q)

    print(q.is_empty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue("")
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue("")

    print(q)

    print(q.make_new_queue(0, 2, 3, 4, 1))
    print(q.make_new_queue(0, 2, 3, 4, 2))
