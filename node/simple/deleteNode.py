#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:05
desc: 删除链表中的节点
tag: 链表
提示：
链表中节点的数目范围是 [2, 1000]
-1000 <= Node.val <= 1000
链表中每个节点的值都是唯一的
需要删除的节点 node 是 链表中的一个有效节点 ，且 不是末尾节点
'''


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 将当前节点的值替换为下一个节点的值，然后把下一个节点删除就等价于删除当前节点
        # 因为当前节点不是末尾节点，而且节点值不会重复
        node.val = node.next.val
        node.next = node.next.next
        
    