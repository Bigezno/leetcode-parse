#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:36
desc: 
tag:
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

'''

class MinStack:

    def __init__(self):
        self.item_list = []

    def push(self, val: int) -> None:
        # 先进后出
        self.item_list.append(val)

    def pop(self) -> None:
        length = len(self.item_list)
        return self.item_list.pop(length - 1)


    def top(self) -> int:
        length = len(self.item_list)
        return self.item_list[length - 1]


    def getMin(self) -> int:
        length = len(self.item_list)
        min_val = self.item_list[0]
        for i in range(1, length):
            if self.item_list[i] < min_val:
                min_val = self.item_list[i]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()