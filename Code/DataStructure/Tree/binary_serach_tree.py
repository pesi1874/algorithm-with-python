#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class NewNode:

    # 构造器，产生一个新节点
    def __init__(self, data):
        self.key = data
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
def insert(node, key):
    if node is None:
        k = NewNode(key)
        return k
    if key == node.key:
        node.count += 1
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# 给予一个非空二叉搜索树，返回该树上的最小节点，注意：不需要搜索整棵树
def min_value_node(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


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
        temp = min_value_node(root.right)
        root.key = temp.key

        #删除右子树作为继承根节点的节点
        root.right = delete_node(root.right, temp.key)

    return root


if __name__ == '__main__':
    root = None
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 9)
    root = insert(root, 11)
    root = insert(root, 10)
    root = insert(root, 12)
    root = insert(root, 12)


    print("Inorder traversal of the given tree")
    inorder(root)
    print()