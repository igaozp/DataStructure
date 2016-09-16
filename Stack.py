class Stack:
    def __init__(self, datas=[]):
        # 使用List保存数据
        self.datas = datas

    def __len__(self):
        # 计算栈内的数据个数
        return len(self.datas)

    def isEmpty(self):
        # 检查栈是否为空
        return len(self) == 0

    def push(self, data):
        # 压栈，添加一个元素
        self.datas.append(data)

    def pop(self):
        # 栈顶元素出栈，如果栈为空则返回None
        return self.datas.pop() if not self.isEmpty() else None

    def peek(self):
        # 查看栈顶元素
        return self[len(self.datas) - 1] if not self.isEmpty() else None