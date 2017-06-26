class Stack:
    def __init__(self, data=[]):
        # 使用List保存数据
        self.data = data

    def __len__(self):
        # 计算栈内的数据个数
        return len(self.data)

    def is_empty(self):
        # 检查栈是否为空
        return len(self) == 0

    def push(self, data):
        # 压栈，添加一个元素
        self.data.append(data)

    def pop(self):
        # 栈顶元素出栈，如果栈为空则返回None
        return self.data.pop() if not self.is_empty() else None

    def peek(self):
        # 查看栈顶元素
        return self[len(self.data) - 1] if not self.is_empty() else None
