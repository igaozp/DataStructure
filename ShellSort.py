def insert_sort(l, start, gap):
    for i in range(start + gap, len(l), gap):
        current_value = l[i]
        pos = i
        while pos >= gap and l[pos - gap] > current_value:
            l[pos] = l[pos - gap]
            pos -= gap
        l[pos] = current_value


def shell_sort(l):
    sublist_count = len(l) / 2
    while sublist_count > 0:
        for pos in range(sublist_count):
            insert_sort(l, pos, sublist_count)
        sublist_count = sublist_count / 2


import random

a = [random.random() for i in range(40)]
print(a)
shell_sort(a)
print(a)
