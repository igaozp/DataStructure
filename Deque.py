class Deque:
    # 双向队列
    def __init__(self, data=[]):
        self.data = data

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def en_queue(self, data):
        # 入队
        self.data.append(data)

    def de_queue(self):
        # 出队
        return self.data.pop(0) if not self.is_empty else None

    def en_queue_front(self, data):
        # 头部入队
        self.data.insert(0, data)

    def de_queue_back(self):
        # 尾部出队
        return self.data.pop() if not self.is_empty else None

    def peek_front(self):
        # 检查队首元素
        return self[0] if not self.is_empty else None

    def peek_back(self):
        # 检查队尾元素
        return self[len(self) - 1] if not self.is_empty else None