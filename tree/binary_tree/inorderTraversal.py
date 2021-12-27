#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:24
TAG: 
desc: 
'''
from typing import List, Optional

from tree.ListNode import TreeNode


class Solution:
    def traversal(self, val_list, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            self.traversal(val_list, root.left)
        val_list.append(root.val)
        if root.right:
            self.traversal(val_list, root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) ->List[int]:
        val_list = []
        self.traversal(val_list, root)
        return val_list

    def innorderTraversal_foreach(self, root:Optional[TreeNode]) ->List[int]:
        # 非递归实现
        val_list = []
        if not root:
            return val_list
        tree_list = []
        while root and tree_list:
            while root:
                tree_list.append(root)
                root = root.left
            if tree_list:
                root = tree_list.pop()
                val_list.append(root.val)
                root = root.right
        return val_list