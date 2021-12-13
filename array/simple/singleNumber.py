#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 18:22
desc: 只出现一次的数字
TAG: 位运算 数组
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

示例 1:
    输入: [2,2,1]
    输出: 1

示例 2:
输入: [4,1,2,1,2]
    输出: 4

解题思路:
    异或运算，相异为真，相同为假，所以 a^a = 0 ;0^a = a
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result
