#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  10:26
desc: 删除排序数组中的重复项
Tag： 数组，双指针
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

提示：
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        解题思路:
            双指针左右移动
        :param nums:
        :return:
        '''
        if not nums or len(nums) == 0:
            return 0
        left = 0
        for right in range(1, len(nums)):
            # 左指针==右指针，则右指针+1,左指针不动；
            if nums[left] == nums[right]:
                continue
            else:
                # 左指针 != 右指针，左指针+1，左指针值=右指针值，
                left += 1
                nums[left] = nums[right]
        return left + 1
