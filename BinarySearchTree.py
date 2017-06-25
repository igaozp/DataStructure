class Node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def clear(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def contain(self, x, node):
        # 查找元素
        if node is None:
            return False
        if x < node.element:
            return self.contain(x, node.left)
        elif x > node.element:
            return self.contain(x, node.right)
        else:
            return True

    def find_min(self, node):
        # 查找最小的元素
        if node is None:
            return None
        elif node.left is None:
            return node
        return self.find_min(node.left)

    def find_max(self, node):
        # 查找最大的元素
        if node is None:
            return None
        elif node.right is None:
            return node
        return self.find_max(node.right)

    def insert(self, x, node):
        # 插入一个元素
        if node is None:
            return Node(x)
        if x < node.element:
            node.left = self.insert(x, node.left)
        elif x > node.element:
            node.right = self.insert(x, node.right)
        return node

    def remove(self, x, node):
        # 删除一个元素
        if node is None:
            return node
        if x < node.element:
            node.left = self.remove(x, node.left)
        elif x > node.element:
            node.right = self.remove(x, node.right)
        elif node.left is not None and node.right is not None:
            node.element = self.find_min(node.right).element
            node.right = self.remove(node.element, node.right)
        else:
            node = node.left if (node.left is not None) else node.right
        return node

    def print_tree(self, node):
        # 中序遍历
        if node is not None:
            self.print_tree(node.left)
            print(node.element)
            self.print_tree(node.right)

    def post_order_print_tree(self, node):
        # 后序遍历
        if node is not None:
            self.post_order_print_tree(node.left)
            self.post_order_print_tree(node.right)
            print(node.element)

    def pre_order_print_tree(self, node):
        # 先序遍历
        if node is not None:
            print(node.element)
            self.pre_order_print_tree(node.left)
            self.pre_order_print_tree(node.right)
