#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
Tag: 链表
date:  10:46
desc:
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头.
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
 每个链表中的节点数在范围 [1, 100] 内
 0 <= Node.val <= 9
 题目数据保证列表表示的数字不含前导零
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        carry_val = 0
        while (l1 is not None or l2 is not None):
            val = carry_val
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry_val = val // 10
            val = val % 10
            node = ListNode(val)
            result.append(node)

        if carry_val == 1:
            result.append(ListNode(1))

        for i in range(0, len(result) - 1):
            result[i].next = result[i + 1]
        return result[0]


if __name__ == '__main__':
    l1 = ListNode(10)
    l2 = ListNode(100)
    l2.next = l1
