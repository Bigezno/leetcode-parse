#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:25
desc: 层级遍历
tag:
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from tree.ListNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        val_list = []
        if not root:
            return val_list
        item_list = [root]
        while item_list:
            current_val_list = []
            size = len(item_list)
            while size:
                tree = item_list.pop(0)
                current_val_list.append(tree.val)
                if tree.left:
                    item_list.append(tree.left)
                if tree.right:
                    item_list.append(tree.right)
                size -= 1
            val_list.append(current_val_list)
        return val_list
