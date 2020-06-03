#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:

    # 构造器，产生一个新节点
    def __init__(self, data):
        """

        :param data:
        """
        self.key = data
        self.count = 1
        self.left = None
        self.right = None


class Tree:

    def __init__(self, root_node):
        self.root_node = root_node

    def insert(self, key):
        pass

    def delete(self, key):
        pass

    def search(self, key):
        pass

    def get_min_key(self, key):
        pass


if __name__ == '__main__':
    root_node = Node(data=10)
    tree = Tree(root_node=root_node)
