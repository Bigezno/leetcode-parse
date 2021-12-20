#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:53
desc: 最大子序和
tag: 数组 分治 动态规划
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        思路过程：
            1. 确定状态  --> dp[n] 表示终点在n的最佳子序列和
            2. 找到转移公式  --> dp[i] = max(dp[i - 1], 0) + num[i];
            3. 确定初始条件以及边界条件 --> dp[0] = 第一个不为0的元素；
            4. 计算结果 --> 最后返回的值应该从dp数组中取最大值
        :param nums:
        :return:
        '''
        dp = [nums[0]]
        max_val = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1], 0) + nums[i])
            max_val = max(dp[i], max_val)
        return max_val




