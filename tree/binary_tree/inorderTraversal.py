#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:23
desc: 中序遍历
tag:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val_list = []
        item_list = []
        while root or item_list:
            while root:
                item_list.append(root)
                root = root.left
            if item_list:
                root = item_list.pop()
                val_list.append(val)
                root = root.right
        return val_list
