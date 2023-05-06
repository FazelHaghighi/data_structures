class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def make_empty(self):
        if self.is_empty():
            return "Stack is empty!"
        self.items = []

    def is_empty(self):
        return not self.items

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def reverse(self):
        if self.is_empty():
            return
        else:
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.is_empty())
    print(s)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(s.is_empty())
    print(s)

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.reverse()

    print(s)

    s.make_empty()

    print(s.is_empty())
