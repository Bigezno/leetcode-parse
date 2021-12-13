#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  19:02
desc: 验证二叉搜索树
tag: 树，二叉搜索树，递归
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        #递归并引入上界，下界来判断是否有效的二叉搜索树
        def check(node, min_val = float('-inf'), max_val = float('inf')) -> bool:
            if not node:
                return True
                #每个节点如果超过这个范围，直接返回false
            if node.val <= min_val or node.val >= max_val:
                return False
            #这里再分别以左右两个子节点分别判断，
             #左子树范围的最小值是minVal，最大值是当前节点的值，也就是root的值，因为左子树的值要比当前节点小
             #右子数范围的最大值是maxVal，最小值是当前节点的值，也就是root的值，因为右子树的值要比当前节点大
            return check(node.left, min_val, node.val) and check(node.right, node.val, max_val)
        return check(root)

    node_pre = None
    def is_valid_bst(self, root: TreeNode) -> bool:
        # 中序递归遍历，中序遍历二叉搜索树，遍历的结果一定是有序的，如果不是则不是二叉搜索树
        if not root:
            return True
        # 访问左子树
        if not self.is_valid_bst(root.left):
            return False
        # //访问当前节点：如果当前节点小于等于中序遍历的前一个节点直接返回false。
        if node_pre and node_pre.val >= root.val:
            return False
        node_pre = root
        # 访问右子树
        if not self.is_valid_bst(root.right):
            return False
        return True