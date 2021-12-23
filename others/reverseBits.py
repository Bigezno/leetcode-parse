#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  22:04
desc: 颠倒二进制位
tag:
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # res先往左移一位，把最后一个位置空出来，
            # 用来存放n的最后一位数字
            res <<= 1  # 右边补0
            # res加上n的最后一位数字
            res |= n & 1  # 任何数&1=任何数，0｜任何数=任何数
            # n往右移一位，把最后一位数字去掉
            n >>= 1
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(100))
    num = 100  # 1100100
