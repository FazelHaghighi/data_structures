class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def inorder(self):
        res = []
        if self.left:
            res = self.left.inorder()
        res.append(self.data)
        if self.right:
            res = res + self.right.inorder()
        return res

    def preorder(self):
        res = [self.data]
        if self.left:
            res = res + self.left.preorder()
        if self.right:
            res = res + self.right.preorder()
        return res

    def BFS(self):
        if self is None:
            return
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def DFS(self):
        if self is None:
            return
        stack = [self]
        while stack:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


if __name__ == "__main__":
    root = Tree(12)
    data_list = [6, 14, 3, 8, 13, 15, 7, 9, 11, 10]
    for data in data_list:
        root.insert(data)

    print("Inorder")
    print(root.inorder())

    print("Preorder")
    print(root.preorder())

    print("BFS")
    root.BFS()

    print("DFS")
    root.DFS()
