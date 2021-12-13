#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 18:18
TAG: 数组 哈希表 排序
desc: 存在重复元素
    给定一个整数数组，判断是否存在重复元素。
    如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
    输入: [1,2,3,1]
    输出: true

示例 2:
    输入: [1,2,3,4]
    输出: false

示例 3:
    输入: [1,1,1,3,3,4,3,2,4,2]
    输出: true

'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        judge_dict = {}
        for num in nums:
            if num not in judge_dict:
                judge_dict[num] = 1
            else:
                return True
        return False