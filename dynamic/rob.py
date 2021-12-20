#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  18:13
desc: 打家劫舍
tag: 数组，动态规划
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''


class Solution:
    def rob(self, nums) -> int:
        '''
        思路过程：
            1. 确定状态  --> dp[n][2] --> dp[i][1]表示第i家偷了的最大总金额；dp[i][0]，表示第i家没偷的最大总金额
            2. 找到转移公式  --> dp[i][1] = nums[i] + dp[i-1][0]
                                dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            3. 确定初始条件以及边界条件 -->
                    dp[0][0] = 0，第一家没有偷；
                    dp[0][1] = nums[0]，第一家偷了。
            4. 计算结果 --> 最后返回的值应该从dp数组中取最大值
        :param nums:
        :return:
        '''
        dp = [[0, 0] for i in range(0, len(nums))]
        print(dp)
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])


s = Solution()
print(s.rob([1, 2, 3]))