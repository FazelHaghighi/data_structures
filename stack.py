class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.items.pop()

    def makeEmpty(self):
        if self.isEmpty():
            return "Stack is empty!"
        self.items = []

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return self.items == 100

    def insertAtBottom(self, item):
        if self.isEmpty():
            self.push(item)
        else:
            temp = self.pop()
            self.insertAtBottom(item)
            self.push(temp)

    def reverse(self):
        if self.isEmpty():
            return
        else:
            temp = self.pop()
            self.reverse()
            self.insertAtBottom(temp)

    def __str__(self) -> str:
        return str(self.items)


from stack import Stack

if __name__ == "__main__":

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.isEmpty())
    print(s)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(s.isEmpty())
    print(s)

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.reverse()

    print(s)

    s.makeEmpty()

    print(s.isEmpty())
