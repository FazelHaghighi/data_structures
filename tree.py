class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
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
        else:
            self.data = data

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def BFS(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while len(q) > 0:
            print(q[0].data)
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def DFS(self, root):
        if root is None:
            return
        s = []
        s.append(root)
        while len(s) > 0:
            print(s[-1].data)
            node = s.pop()
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)


if __name__ == "__main__":
    root = Tree(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    root.insert(13)
    root.insert(15)
    root.insert(7)
    root.insert(9)
    root.insert(11)
    root.insert(10)

    print("Inorder")
    print(root.inorder(root))

    print("Preorder")
    print(root.preorder(root))

    print("BFS")
    root.BFS(root)

    print("DFS")
    root.DFS(root)
