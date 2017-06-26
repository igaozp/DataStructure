class TreeNode:
    """根节点的深度为1，叶子结点的高度为1，非叶子节点的高度为其子树高度的最大值加1"""
    def __init__(self, data, left=None, right=None, height=1):
        self.data = data
        self.left = left
        self.right = right
        self.height = height

    def __str__(self):
        return "tree node %s with height %d" % (self.data, self.height)


def height(node):
    return node.height if node else 0


class AVLTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert_root(self, data):
        self.root = self.insert(data, self.root)

    def insert(self, data=None, node=None):
        if not node:
            return TreeNode(data)
        if data < node.data:
            # 插在左子树上
            node.left = self.insert(data, node.left)
            if height(node.left) - height(node.right) == 2:
                if data < node.left.data:
                    node = self.rotate_with_left_child(node)
                else:
                    node = self.double_with_left_child(node)
        else:
            # 插在右子树上
            node.right = self.insert(data, node.right)
            if height(node.right) - height(node.left) == 2:
                if data > node.right.data:
                    node = self.rotate_with_right_child(node)
                else:
                    node = self.double_with_right_child(node)
                    node.height = max(height(node.left), height(node.right)) + 1
        return node
    
    def rotate_with_left_child(self, k2):
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = max(height(k2.left), height(k2.right)) + 1
        k1.height = max(height(k1.left), height(k2)) + 1
        return k1

    def double_with_left_child(self, k3):
        k3.left = self.rotate_with_right_child(k3.left)
        return self.rotate_with_left_child(k3)

    def rotate_with_right_child(self, k1):
        k2 = k1.right
        k1.right = k2.left
        k2.left = k1
        k1.height = max(height(k1.left), height(k1.right)) + 1
        k2.height = max(height(k1), height(k2.right)) + 1
        return k2

    def double_with_right_child(self, k1):
        k1.right = self.rotate_with_left_child(k1.right)
        return self.rotate_with_right_child(k1)
