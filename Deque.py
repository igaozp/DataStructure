class Deque:
    def __init__(self, datas=[]):
        self.datas = datas

    def __len__(self):
        return len(self.datas)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data):
        # 入队
        self.datas.append(data)

    def dequeue(self):
        # 出队
        return self.datas.pop(0) if not self.isEmpty else None

    def enqueueFront(self, data):
        # 头部入队
        self.datas.insert(0, data)

    def dequeueBack(self):
        # 尾部出队
        return self.datas.pop() if not self.isEmpty else None

    def peekFront(self):
        # 检查队首元素
        return self[0] if not self.isEmpty else None

    def peekBack(self):
        # 检查队尾元素
        return self[len(self) - 1] if not self.isEmpty else None