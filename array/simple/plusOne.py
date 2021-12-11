#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 19:11
desc: 加一
TAG: 数组 数学
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
    输入：digits = [1,2,3]
    输出：[1,2,4]
    解释：输入数组表示数字 123。

示例 2：
    输入：digits = [4,3,2,1]
    输出：[4,3,2,2]
    解释：输入数组表示数字 4321。

示例 3：
    输入：digits = [0]
    输出：[1]

提示：
    1 <= digits.length <= 100
    0 <= digits[i] <= 9

'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry_cal = 0
        for i in reversed(range(len(digits))):
            if i == len(digits) - 1:
                digits[i] += 1
            val = (digits[i] + carry_cal) % 10
            carry_cal = (digits[i] + carry_cal) // 10
            result.append(val)
        if carry_cal == 1:
            result.append(1)
        result.reverse()
        return result

if __name__ == '__main__':
    s = Solution()
    digits = [1,2,3]
    nums = s.plusOne(digits)
    print(nums)