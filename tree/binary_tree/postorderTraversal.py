#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  16:53
desc: 后序遍历
tag:
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from tree.ListNode import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val_list = []
        if not root:
            return val_list
        item_list = [root]
        while item_list:
            tree = item_list.pop()
            val_list.append(tree.val)
            if tree.left:
                item_list.append(tree.left)
            if tree.right:
                item_list.append(tree.right)
        return val_list[::-1]

