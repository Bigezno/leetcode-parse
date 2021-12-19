#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:22
desc: 将有序数组转换为二叉搜索树
tag:树 二叉搜索树 数组 分治 二叉树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        if len(nums) > 1:
            root.left = self.sortedArrayToBST(nums[0:mid_index])
        if mid_index + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[mid_index+1:])
        return root

if __name__ == '__main__':
    print([0][0:1])
    print([0,1,2,3,4,5][3:])
    nums = [-10,-3,0,5,9]
    s = Solution()

    node_list = []
    root = s.sortedArrayToBST(nums)
    node_list.append(root)
    while node_list:
        node = node_list.pop(0)
        print(node.val)
        if node.left:
            node_list.append(node.left)
        if node.right:
            node_list.append(node.right)

