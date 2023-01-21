class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items.pop(0)

    def makeEmpty(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def makeNewQueue(self, queue, firstFront, firstRear, secondFront, secondRear, n):
        newQueue = Queue()
        if n == 1:
            for i in range(firstFront, firstRear):
                newQueue.enqueue(self.items[i])
        if n == 2:
            for i in range(secondFront, secondRear):
                newQueue.enqueue(self.items[i])
        return newQueue

    def __str__(self) -> str:
        return str(self.items)


from queue import Queue

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.isEmpty())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.isEmpty())
    print(q)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.makeEmpty()

    print(q)

    print(q.isEmpty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue("")
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue("")

    print(q)

    print(q.makeNewQueue(q, 0, 2, 3, 4, 1))
    print(q.makeNewQueue(q, 0, 2, 3, 4, 2))
