#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  16:49
desc: 买卖股票的最佳时机
tag: 动态规划
给定一个数组 prices ，它的i 个元prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        思路过程：
            1. 确定状态
            2. 找到转移公式
            3. 确定初始条件以及边界条件
            4. 计算结果
        '''
        if not list:
            return 0
        max_prices = 0
        min_value = prices.pop(0)
        for price in  prices:
            min_value = min(min_value, price)
            max_prices = max(price - min_value, max_prices)
        return max_prices
