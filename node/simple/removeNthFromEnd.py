#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  00:36
desc: 删除链表的倒数第N个节点
tag: 链表 双指针
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        count = 0
        while node:
            count += 1
            node = node.next

        # 删除头节点
        last = count - n
        if last == 0:
            return head.next

        # 找到前last-1的节点，
        node = head
        for i in range(0, last-1):
            node = node.next
        node.next = node.next.next
        return head

    # 获取节点所在位置，逆序
    def get_length(self, node, n):
        if not node:
            return 0
        pos = self.get_length(node.next, n) + 1
        # 获取要删除链表的前一个结点，就可以完成链表的删除
        if pos == n + 1:
            node.next = node.next.next
        return pos


    def removeNthFromEnd_v2(self, head: ListNode, n: int) -> ListNode:
        pos = self.get_length(head, n)
        if pos == n:
            return head.next
        return head




