import random


def insert_sort(l):
    # 插入排序
    for i in range(1, len(l)):
        temp = l[i]
        j = i
        while j > 0 and temp < l[j - 1]:
            l[j] = l[j - 1]
            j -= 1
        l[j] = temp

a = [random.random() for i in range(40)]
insert_sort(a)
print(a)
