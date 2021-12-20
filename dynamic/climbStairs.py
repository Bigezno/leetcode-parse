#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  00:32
desc: 爬楼梯
tag:记忆化搜索 数学 动态规划
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        动态转移方程：
            d1 = 1
            d2 = 2
            d3 = 3
            d4 = 5
            dn = d[n-1] + d[n-2]
        :param n:
        :return:
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 由于不是尾递归，效率会很低；
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


    def __init__(self):
        self.memo = {}

    def climbStairs_v2(self, n: int) -> int:
        # 备忘录解法，自顶向下，递归调用
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n not in self.memo.keys():
            self.memo[n] = self.climbStairs_v2(n - 1) + self.climbStairs_v2(n - 2)
        return self.memo[n]


    def climbStairs_v3(self, n: int) -> int:
        # 动态规划--> 找出状态转移方程，然后自底向上求解；
        db[1] = 1
        db[2] = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n):
            db[i] = db[i - 1] + db[i - 2]
        return db[n - 1] + db[n - 2]


s = Solution()
print(s.climbStairs(20))
print(s.climbStairs_v2(20))

