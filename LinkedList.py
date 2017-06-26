class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


class LinkedList:
    def __init__(self, data=None):
        # 链表初始化
        if data is None:
            self.head = None
        else:
            self.head = Node(data[0])
            p = self.head
            for i in data[1:]:
                node = Node(i)
                p.next = node
                p = p.next
    
    def __len__(self):
        if self.head is None:
            return 0
        p = self.head
        result = 0
        while p is not None:
            p = p.next
            result += 1
        return result
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            return None
        if self.head is None:
            return None
        p = self.head
        j = 0
        while j < index:
            p = p.next
            j += 1
        return p.data

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            return
        if self.head is None:
            return
        p = self.head
        j = 0
        while j < index:
            p = p.next
            j += 1
        p.data = value

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def insert(self, index, data):
        if data is None:
            return
        if index < 0 or index > len(self):
            return
        
        if index == 0:
            q = Node(data, self.head)
            self.head = q
            return
        
        p = self.head
        post = self.head
        j = 0
        while j < index:
            post = p
            p = p.next
            j += 1
            if index == j:
                q = Node(data, p)
                post.next = q

    def delete(self, index):
        if index < 0 or index >= len(self):
            return None
        if self.head is None:
            return None
        if index == 0:
            result = self.head.data
            self.head = self.head.next
            return result
        p = self.head
        j = 0
        while j < index - 1:
            p = p.next
            j += 1
        result = p.next.data
        p.next = p.next.next
        return result
