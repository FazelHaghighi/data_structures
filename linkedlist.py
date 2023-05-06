class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    @classmethod
    def bind(cls, list1, list2):
        linked_list = cls()

        if list1.size() > list2.size():
            main_temp = list1.head
            temp = list2.head
        else:
            main_temp = list2.head
            temp = list1.head

        while main_temp:
            linked_list.push_back(main_temp.data)
            main_temp = main_temp.next
            if temp:
                linked_list.push_back(temp.data)
                temp = temp.next

        return linked_list

    @classmethod
    def convert(cls, linked_list):
        temp = linked_list.head
        temp_back = linked_list.head.prev

        while temp:
            temp.prev = temp_back
            temp_back = temp
            temp = temp.next

        tail = temp_back
        return cls(head=linked_list.head, tail=tail)

    def size(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        return size

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def get_by_pos(self, pos):
        temp = self.head
        for i in range(0, pos + 1):
            if i == pos and self.head:
                return self.head.data
            else:
                if self.head.next:
                    self.head = self.head.next
                else:
                    return None

    def delete_by_pos(self, pos):
        temp = self.head
        if not temp:
            return None
        elif pos == 0:
            self.pop_front()
            return
        else:
            for i in range(pos + 1):
                if i == pos and temp:
                    temp_front = temp.next
                    temp_back = temp.prev
                    temp_front.prev = temp_back
                    temp_back.next = temp_front
                    temp_back = temp_front = temp = None
                    return
                else:
                    if temp.next:
                        temp = temp.next
                    else:
                        return None

    def push_back(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def peek_front(self):
        if not self.head:
            return None
        else:
            return self.head.data

    def peek_back(self):
        if not self.tail:
            return None
        else:
            return self.tail.data

    def pop_front(self):
        if not self.head:
            return None
        else:
            temp = self.head
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            temp.next = None
            return temp.data

    def pop_back(self):
        if not self.tail:
            return None
        else:
            temp = self.tail
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            temp.prev = None
            return temp.data

    def insert_after(self, node, data):
        if not node:
            return None

        new_node = Node(data)
        new_node.prev = node

        if node == self.tail:
            self.tail = new_node
        else:
            new_node.next = node.next
            new_node.next.prev = new_node

        node.next = new_node

    def __str__(self) -> str:
        if not self.head:
            return "The list is empty!"
        
        n = self.head
        string = ""
        while n is not None:
            string += str(n.data) + " "
            n = n.next

        return string


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    list1.push_back(1)
    list1.push_back(2)
    list1.push_back(3)
    list1.push_back(4)

    list2.push_back(11)
    list2.push_back(12)
    list2.push_back(13)
    list2.push_back(14)

    print("list1: ", list1)
    print("list2: ", list2)

    list3 = DoublyLinkedList.bind(list1, list2)
    print("list3: ", list3)

    list1 = DoublyLinkedList.convert(list1)
    print("list1: ", list1)

