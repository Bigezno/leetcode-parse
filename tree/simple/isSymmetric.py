#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  22:44
desc: 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
tag: 树，递归
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_symmetric_tree(self, left: TreeNode, right: TreeNode) -> bool:
        # 两个子节点都为空
        if not left and not right:
            return True
        # 如果存在一个子节点为空，另一个不为空；或者两个子节点的值不相等。
        if (not left and right) or (left and not right) or (left.val != right.val):
            return False
        return self.is_symmetric_tree(left.left, right.right) and self.is_symmetric_tree(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归方式
        # 判断二叉树是否是对称，需要从子节点开始比较，两个子节点的值必须相同，并且左子节点的右子节点（如果有）必
        # 须等于右子节点的左子节点，左子节点的左子节点必须等于右子节点的右子节点。
        if not root:
            return False
        return self.is_symmetric_tree(root.left, root.right)


    def is_symmetric_v2(self, root:TreeNode) -> bool:
        if not root:
            return False
        node_list = []
        node_list.append(root.left)
        node_list.append(root.right)
        while node_list:
            left = node_list.pop()
            right = node_list.pop()
            if not left and not right:
                continue
            # 如果存在一个子节点为空，另一个不为空；或者两个子节点的值不相等。
            if (not left and right) or (left and not right) or (left.val != right.val):
                return False
            # 要记录入栈的顺序，左子节点的左节点要和右子节点的右节点比较
            node_list.append(left.left)
            node_list.append(right.right)
            node_list.append(left.right)
            node_list.append(right.left)
        return True