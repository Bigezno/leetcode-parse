#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:52
desc: 回文链表
tag:栈 递归 链表 双指针
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 利用list翻转解法
        item_list = []
        while head:
            item_list.append(str(head.val))
            head = head.next
        val_string = "".join(item_list)
        item_list.reverse()
        reverse_string = "".join(item_list)
        return val_string == reverse_string


    def isPalindromev2(self, head: ListNode) -> bool:
        # list + 双指针解法
        item_list = []
        while head:
            item_list.append(str(head.val))
            head = head.next

        left = 0
        right = len(item_list) - 1
        while left < right:
            if item_list[left] != item_list[right]:
                return False
            left += 1
            right -= 1
        return True

    def __init__(self):
        self.temp = None

    def check(self, head):
        if not head:
            return True
        pos = check(head.next) and (head.val == self.temp.val)
        self.temp = self.temp.next
        return pos

    def isPalindromev3(self, head: ListNode) -> bool:
        # 递归解法
        self.temp = head
        return check(head)