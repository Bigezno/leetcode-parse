#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  11:25
desc:  位1的个数
tag: 位运算
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
与运算：1&1=1, 1&0=0, 0&0=0;
或运算：1|1=1, 1|0=1, 0|0=0
非运算：取反;
异或：a^a=0, 0^0=0,a^0=a;
左移：全部左移，低位补0; 等价于整除2；
右移：全部右移，高位补0; 等价于乘以2；
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            print(n)
            count += (n & 1)
            n = n >> 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(11111111111111111111111111111101))