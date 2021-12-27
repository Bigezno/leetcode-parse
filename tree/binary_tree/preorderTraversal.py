#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  16:23
TAG: 
desc: 前序遍历
'''
from typing import Optional, List

from tree.ListNode import TreeNode


class Solution:

    def traversal(self, val_list: List[int], root: TreeNode):
        if not root:
            return
        val_list.append(root.val)
        if root.left:
            self.traversal(val_list, root.left)
        if root.right:
            self.traversal(val_list, root.right)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归算法->前序遍历: 根节点 -> 左节点 -> 右节点
        val_list = []
        self.traversal(val_list, root)
        return val_list

    def preorderTraversal_foreach(self, root: Optional[TreeNode]) -> List[int]:
        # 利用栈先进后出，所以每个右节点是最后访问，所以最先进入;
        val_list = []
        if not root:
            return val_list
        tree_list = [root]
        while tree_list:
            node = tree_list.pop()
            val_list.append(root.val)
            if node.right:
                tree_list.append(node.right)
            if node.left:
                tree_list.append(node.left)
