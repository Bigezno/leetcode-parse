#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  13:44
desc: 反转链表
tag: 递归 链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''

import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 空
        if not head:
            return head
        node_list = []
        tmp = head
        while tmp:
            node_list.append(tmp)
            tmp = tmp.next
        node_list.reverse()
        for i in range(len(node_list)):
            if i == len(node_list) - 1:
                node_list[i].next = None
            else:
                node_list[i].next = node_list[i+1]
        return node_list[0]



    def reverse(self, head: ListNode) -> ListNode:
        # 递归解法
        if not head:
            return head
        node = self.reverse(head.next)
        if node:
            node.next = head
        # 则head为头节点
        head.next = None
        return head

    def reverseListV2(self, head: ListNode) -> ListNode:
        # 空或者只有一个节点
        if not head or not head.next:
            return head
        # 翻转节点即为头节点
        reversed_node = self.reverseListV2(head.next)
        # 将下一个节点指向自己
        head.next.next = head
        # 末尾节点要置空，否则会置环
        head.next = None
        return reversed_node


    def last_reverse(self, head, new_head):
        #  尾递归, 在递归返回前处理逻辑，像v2就不是尾递归，因为逻辑处理放在了递归返回的后面
        if not head:
            return new_head
        next_node = head.next
        head.next = new_head
        return self.last_reverse(next_node, head)


    def reverseListv4(self, head: ListNode) -> ListNode:
        # 递归方式
        return self.last_reverse(head, None)


    def reverseListv3(self, head: ListNode) -> ListNode:
        # 双指针解法
        left = None
        right = head
        while right:
            tmp = right
            right = right.next
            tmp.next = left
            left = tmp
        return left



if __name__ == '__main__':
    s = Solution()
    list_node_1 = ListNode(1)
    list_node_2 = ListNode(2)
    list_node_3 = ListNode(3)
    list_node_4 = ListNode(4)
    list_node_5 = ListNode(5)

    list_node_1.next = list_node_2
    list_node_2.next = list_node_3
    list_node_3.next = list_node_4
    list_node_4.next = list_node_5

    node = s.reverseListV2(list_node_1)

    while node:
        print(node.val)
        node = node.next