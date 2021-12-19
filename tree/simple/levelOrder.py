#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  22:58
desc: 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
tag: 树，广度优先搜索，二叉树
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs遍历
        if not root:
            return []
        result_list = []
        foreach_list = []
        foreach_list.append(root)
        while foreach_list:
            node_list = []
            # 每一层的节点数
            level_size = len(foreach_list)
            for i in range(level_size):
                node = foreach_list.pop(0)
                node_list.append(node.val)
                if node.left:
                    foreach_list.append(node.left)
                if node.right:
                    foreach_list.append(node.right)
            if node_list:
                result_list.append(node_list)
        return result_list
