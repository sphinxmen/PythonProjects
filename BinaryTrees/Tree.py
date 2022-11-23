class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node(Data={self.data}, Left={self.left}, Right={self.right})'

    def __repr__(self):
        return self.__str__()

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right


class BinaryTree:

    def __init__(self, root=None):
        self.root = TreeNode(root)

    def __str__(self):
        return f'BinaryTree({self.root})'

    def __repr__(self):
        return f'BinaryTree({self.root})'

    def insert(self, data):
        # Проверка пустое ли дерево
        if self.root.get_data() is None:
            return self.root.set_data(data)
        new_node = TreeNode(data)
        current = self.root
        while True:
            if data < current.get_data():
                if current.get_left() is None:
                    return current.set_left(new_node)
                current = current.get_left()
                continue
            elif data > current.get_data():
                if current.get_right() is None:
                    return current.set_right(new_node)
                current = current.get_right()
                continue
            return

    # метд удаления
    def delete(self, node):
        pass


def main():
    myTree = BinaryTree()
    myTree.insert(5)
    myTree.insert(3)
    myTree.insert(4)
    myTree.insert(2)
    myTree.insert(8)
    myTree.insert(9)
    myTree.insert(6)
    print(myTree)


main()
