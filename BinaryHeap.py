class Heap:
    def __init__(self, data=[]):
        self.data = data

    def build_heap(self):
        for i in range(len(self) / 2 - 1, -1, -1):
            self.percolate_down(i)

    def percolate_down(self, i):
        temp = self[i]
        while i * 2 + 1 < len(self):
            child = 2 * i + 1
            if child + 1 < len(self) and self[child + 1] < self[child]:
                child += 1
            if self[child] < temp:
                self[i] = self[child]
                i = child
            else:
                break
        self[i] = temp

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self[0] if not self.is_empty() else None

    def delete_min(self):
        if self.is_empty():
            return None
        min_item = self[0]
        self[0] = self.data.pop()
        self.percolate_down(0)
        return min_item

    def insert(self, data):
        hole = len(self)
        self.data.append(data)
        while hole > 0 and data < self[(hole + 1) / 2 - 1]:
            self[hole] = self[(hole + 1) / 2 - 1]
            hole = (hole + 1) / 2 - 1
        self[hole] = data

    def __getitem__(self, i):
        return self.data[i]

    def __setitem__(self, i, y):
        self.data[i] = y
