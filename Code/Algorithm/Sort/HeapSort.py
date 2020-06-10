import random

"""
实现：
堆排序当插入新数据时，数据先添加在列表末尾（实际上是按照完全二叉树的规则放置节点），依次比较该数据与父节点数据的大小，再决定是否交换数据

节点排序方式：
    循环实现
    递归实现

计算规则：
    根据节点的索引获取父节点索引：p_index = array[(index-1)/2] 或 p_index = 
    根据节点的索引获取左子节点索引：l_index = array[(2*inidex)+1]
    根据节点的索引获取右子节点索引：r_index = array[(2*inidex)+2]
"""


class MaxHeap:

    def __init__(self):
        self._data = []
        self._count = len(self._data)

    def build_heap(self, collection):
        """
        接收一个集合，建立堆
        :return:
        """
        self._data = list(collection)
        self._count = len(collection)

    def insert(self, item):
        self._data.append(item)
        self._count += 1
        self.shift_up(self._count - 1)

    def pop(self):
        if self._count > 0:
            ret = self._data[0]
            self._data[0] = self._data[self._count - 1]
            self._count -= 1

            return ret

    def shift_up(self, index):
        if index > 0:
            p_index = int((index - 1) / 2)
            if self._data[index] > self._data[p_index]:
                self._data[index], self._data[p_index] = self._data[p_index], self._data[index]
                self.shift_up(p_index)

    def shift_down(self, index):
        j = (index << 1) + 1
        while j < self._count:
            if j + 1 < self._count and self._data[j + 1] > self._data[j]:
                j += 1
            if self._data[index] >= self._data[j]:
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = (index << 1) + 1

    def search(self, key):
        for index, key in enumerate(self._data):
            if i == key:
                return self._data

    def display(self):
        print(self._data)


if __name__ == '__main__':
    h = MaxHeap()
    for i in range(10):
        h.insert(i)
    h.insert(9)
    h.display()


