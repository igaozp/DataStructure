class Queue:
    def __init__(self, data=[]):
        # 使用List存放数据
        self.data = data

    def __len__(self):
        # 计算队列长度
        return len(self.data)

    def is_empty(self):
        # 判断队列是否为空
        return len(self) == 0

    def enqueue(self, data):
        # 入队
        self.data.append(data)

    def de_queue(self):
        # 出队
        return self.data.pop(0) if not self.is_empty else None

    def peek(self):
        # 检查队首元素
        return self[0] if not self.is_empty() else None
