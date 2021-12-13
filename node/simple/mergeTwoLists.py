#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  15:28
desc: 合并两个有序链表
tag: 链表，递归
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        # 初始化一个新的链表，将值较小的节点追加到新的链表末尾，最后剩余的list加入到末尾，返回新的节点即可。
        new_head = ListNode(0)
        cur = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
        return new_head.next

    def mergeTwoListsv2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归方式
        if not list1:
            return list2
        if not list2:
            return list1
        # 单次递归方法，比较当前节点值
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsv2(list1.next, list2)
            return list1
        if list1.val > list2.val:
            list2.next = self.mergeTwoListsv2(list1, list2.next)
            return list2
