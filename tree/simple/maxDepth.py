#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  18:44
desc: 二叉树的最大深度
tag:树 深度优先搜索 广度优先搜索 二叉树
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归解法
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def bfs(self, root: TreeNode) -> int:
        # 层次遍历，广度优先搜索
        if not root:
            return 0
        queue = []
        queue.append(root)
        count = 0
        while len(queue) != 0:
            count += 1
            # 每一层的个数
            size = len(queue)
            while size > 0:
                size -= 1
                cur = queue.pop()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return count

    def dfs(self, root: TreeNode) -> int:
        # 深度优先搜索
        if not root:
            return 0
        return 0
