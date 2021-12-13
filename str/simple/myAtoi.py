#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  20:51
desc: 字符串转换整数 (atoi)
tag: 字符串
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：
    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        symbol = 1
        item = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == "+" or s[i] == "-"):
                if s[i] == "-":
                    symbol = -1
                continue

            if not str(s[i]).isdigit():  # 不是数字
                break
            # 超过整形最大数字
            if symbol == 1 and (item > 214748364 or (item == 214748364 and int(s[i]) > 7)):
                return 2147483647
            if symbol == -1 and (-item < -214748364 or (-item == -214748364 and int(s[i]) > 8)):
                return -2147483648
            item = item * 10 + int(s[i])

        return item * symbol
        # 214748364 最大数字



if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("42"))



