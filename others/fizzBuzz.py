#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:43
desc: 
tag:
给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
answer[i] == "Fizz" 如果 i 是 3 的倍数。
answer[i] == "Buzz" 如果 i 是 5 的倍数。
answer[i] == i （以字符串形式）如果上述条件全不满足。
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        item_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                item_list.append("FizzBuzz")
            elif i % 3 == 0:
                item_list.append("Fizz")
            elif i % 5 == 0:
                item_list.append("Buzz")
            else:
                item_list.append(str(i))
        return item_list