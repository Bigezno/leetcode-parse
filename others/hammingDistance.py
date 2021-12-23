#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  21:48
desc: 汉明距离
tag: 位运算
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

输入：x = 1, y = 4
输出：2
解释：
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x != 0 and y != 0:
            num_x = x & 1
            num_y = y & 1
            if num_x != num_y:
                count += 1
            x = x >> 1
            y = y >> 1

        while x != 0:
            count += (x & 1)
            x = x >> 1

        while y != 0:
            count += (y & 1)
            y = y >> 1

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 3))
    print(s.hammingDistance(1, 4))