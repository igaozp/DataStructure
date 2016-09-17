class Queue:
    def __init__(self, datas=[]):
        # 使用List存放数据
        self.datas = datas

    def __len__(self):
        # 计算队列长度
        return len(self.datas)

    def isEmpty(self):
        # 判断队列是否为空
        return len(self) == 0

    def enqueue(self, data):
        # 入队
        self.datas.append(data)

    def dequeue(self):
        # 出队
        return self.datas.pop(0) if not self.isEmpty else None

    def peek(self):
        # 检查队首元素
        return self[0] if not self.isEmpty() else None