#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  16:23
desc: 前序遍历
tag:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, val_list, root):
        if not root:
            return
        val_list.append(root.val)
        if root.left:
            self.traversal(val_list, root.left)
        if root.right:
            self.traversal(val_list, root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val_list = []
        self.traversal(val_list, root)
        return val_list