#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
堆的父节点根子节点存在如下关系：
    当父节点的索引为1时，做子节点

"""


class Heap:
    def __init__(self):
        self.h = []
        self.curr_size = 0

    def get_left_child_index(self, i):
        left_child_index = 2 * i + 1
        if left_child_index < self.curr_size:
            return left_child_index

    def get_right_child_index(self, i):
        right_child_index = 2 * i + 2
        if right_child_index < self.curr_size:
            return right_child_index

    def max_heapify(self, index):
        if index < self.curr_size:
            largest = index
            lc = self.get_left_child_index(index)
            rc = self.get_right_child_index(index)
            if lc is not None and self.h[lc] > self.h[largest]:
                largest = lc
            if rc is not None and self.h[rc] > self.h[largest]:
                largest = rc
            if largest != index:
                self.h[largest], self.h[index] = self.h[index], self.h[largest]
                self.max_heapify(largest)

    def build_heap(self, collection):
        self.curr_size = len(collection)
        self.h = list(collection)
        if self.curr_size <= 1:
            return
        for i in range(self.curr_size // 2 - 1, -1, -1):
            self.max_heapify(i)

    def display(self):
        print(self.h)


if __name__ == '__main__':
    c = [i for i in range(10)]
    print(c)
    h = Heap()
    h.build_heap(c)
    h.display()
    h = Heap()

