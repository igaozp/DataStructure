class Stack:
    def __init__(self, datas=[]):
        self.datas = datas

    def __len__(self):
        return len(self.datas)

    def isEmpty(self):
        return len(self) == 0

    def push(self, data):
        self.datas.append(data)

    def pop(self):
        return self.datas.pop() if not self.isEmpty() else None

    def peek(self):
        return self[len(self.datas) - 1] if not self.isEmpty() else None