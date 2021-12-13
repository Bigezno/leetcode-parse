#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  18:10
desc: 环形链表
tag: 哈希表 链表 双指针
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 如果值是唯一的，那么只要将值放入list，判断后续是否存在相同值就能判断了；
        # 快慢指针，慢指针走1步，快指针走2步
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fase.next.next
        return False

    def hasCyclev2(self, head: ListNode) -> bool:
        # 逐个删除法，让其自己指向自己，当循环到最后一个节点，如果没有环，则该节点是指向None，有环则表示指向自己
        if not head or not head.next:
            return False
        if head.next == head:
            return True
        next_node = head.next
        head.next = head
        return self.hasCyclev2(next_node)
