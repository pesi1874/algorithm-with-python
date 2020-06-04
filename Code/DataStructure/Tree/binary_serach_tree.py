#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二叉搜索树的特性主要有：插入，删除，搜索
依赖：递归或循环
问题：使用递归较简洁，但是递归层次过多容易消耗内存堆栈溢出
遍历方式：
递归：前序遍历，中序遍历，后序遍历，
层序遍历
"""


class Node:

    # 构造器，产生一个新节点
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None


# 按顺序遍历树节点
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, "(", root.count, ")", end=" ")
        inorder(root.right)


# 插入新节点
def insert_node(node, key):
    if node is None:
        k = Node(key)
        return k
    if key == node.key:
        node.count += 1
    if key < node.key:
        node.left = insert_node(node.left, key)
    else:
        node.right = insert_node(node.right, key)

    return node


# 给予一个非空二叉搜索树，返回该树上的最小节点，注意：不需要搜索整棵树
def min_node(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def max_node(node: Node):
    current = node
    while current.right is not Node:
        current = current.right

    return current


def search_node(node: Node, key: int):
    if key == node.key:
        return node.count
    if key < node.key:
        return search_node(node.left, key)
    if key > node.key:
        return search_node(node.right, key)
    else:
        print("key: {}, not in tree".format(key))
        return None


def delete_node(root, key):
    if root is None:
        return root

    # 当key比root.key小，则key在左子树上
    if key < root.key:
        root.left = delete_node(root.left, key)

    # 当key比root.key大，则key在右子树上
    elif key > root.key:
        root.right = delete_node(root.right, key)

    # 当key等于root.key
    else:
        # 当key的计数大于1，则计数减一
        if root.count > 1:
            root.count -= 1
            return root

        # 当左子树为空，则返回右子树
        if root.left is None:
            temp = root.right
            return temp
        # 当右子树为空，则返回左子树
        elif root.right is None:
            temp = root.left
            return temp

        # 当左右子树均不为空，复制获取右子树的最小key作为继承的根节点
        temp = min_node(root.right)
        root.key = temp.key

        # 删除右子树作为继承根节点的节点
        root.right = delete_node(root.right, temp.key)

    return root


if __name__ == '__main__':
    root = Node(3)
    insert_node(root, 10)
    insert_node(root, 1)

    print("Inorder traversal of the given tree")
    inorder(root)
