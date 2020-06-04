#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉搜索树的特性主要有：插入，删除，搜索
依赖：递归或循环
问题：使用递归较简洁，但是递归层次过多容易消耗内存堆栈溢出

"""

class Node:

    # 构造器，产生一个新节点
    def __init__(self, key):
        """

        :param data:
        """
        self.key = key
        self.count = 1
        self.left = None
        self.right = None


class Tree:

    def __init__(self, root_node: Node):
        self.tree = root_node

    def insert(self, key):
        if key == self.tree.key:
            self.tree.count += 1
        if key < self.tree.key:
            while self.tree.left != Node:

        else:
            self.tree.right = Node(key)

    def delete(self, key):
        if key < self.tree.

    def search(self, key):
        pass

    def get_min_key(self, key):
        pass


if __name__ == '__main__':
    node = Node(key=10)
    tree = Tree(root_node=node)
    tree.insert(key=20)
    tree.insert(key=1)
    print(tree.tree.left.key)
    print(tree.tree.right.key)

