class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
            self.tail = None
            return
        
        if len(data) == 1:
            node = Node(data[0])
            self.head = node
            self.tail = self.head
            return
        
        self.head = Node(data[0])
        self.tail = Node(data[-1])
        p = self.head

        for data in data[1:-1]:
            q = Node(data)
            p.next = q
            q.prev = p
            p = q

        p.next = self.tail
        self.tail.prev = p

    def __len__(self):
        if self.head is None:
            return 0
        p = self.head
        result = 0
        while p is not None:
            p = p.next
            result += 1
        return result

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def insert(self, index, data):
        if data is None:
            return

        if index < 0 or index > len(self):
            return

        if self.is_empty() and index == 0:
            q = Node(data)
            self.head = q
            self.tail = self.head
            return
        
        # 在头部插入
        if index == 0:
            q = Node(data, self.head, None)
            self.head.prev = q
            self.head = q
            return

        # 在尾部插入
        if index == len(self):
            q = Node(data, None, self.tail)
            self.tail.next = q
            self.tail = q
            return

        # 靠近头部插入
        if index <= len(self) / 2:
            j = 0
            p = self.head
            post = self.head
            while j < index:
                post = p
                p = p.next
                j += 1
            q = Node(data, p, post)
            post.next = q
            p.prev = q
            return

        # 靠近尾部插入
        if index > len(self) / 2:
            j = len(self)
            p = self.tail
            post = self.tail
            while j > index:
                post = p
                p = p.prev
                j -= 1
            q = Node(data, post, p)
            post.prev = q
            p.next = q

    def delete(self, index):
        if index < 0 or index >= len(self):
            return
        
        # 删除表头
        if index == 0:
            result = self.head.data
            self.head = self.head.next
            return result

        # 删除表尾
        if index == len(self) - 1:
            result = self.tail.data
            self.tail = self.tail.prev
            return result

        # 删除靠近头部的元素
        if index <= len(self) / 2:
            j = 0
            p = self.head
            post = self.head
            while j < index:
                post = p
                p = p.next
                j += 1
            post.next = p.next
            p.next.prev = post
            return p.data

        # 删除靠近尾部的元素
        if index > len(self) / 2:
            j = len(self) - 1
            p = self.tail
            post = self.tail
            while j > index:
                post = p
                p = p.prev
                j = j - 1
            post.prev = p.prev
            p.prev.next = post
            return p.data