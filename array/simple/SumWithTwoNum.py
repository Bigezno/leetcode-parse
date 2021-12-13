#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  10:20
desc:
TAG: 数组
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 基础解法，O(n2)
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
        return result

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 进阶解法,2n
        result = []
        num_map = {}
        for i in range(0, len(nums)):
            num_map[nums[i]] = i
        for i in range(0, len(nums)):
            if (target - nums[i]) in num_map.keys() and num_map[target - nums[i]] != i:
                result.append(i)
                result.append(num_map[target - nums[i]])
                break
        return result
