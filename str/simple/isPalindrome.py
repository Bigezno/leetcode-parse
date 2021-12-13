#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  20:39
desc: 验证回文串
tag:双指针 字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例1：
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: "race a car"
输出: false
解释："raceacar" 不是回文串

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 循环s字符串，判断该字符是否是数字或者字母，如果不是则丢弃，是则加入列表
        # 将列表转为字符串1，将列表翻转后转为字符串2，判断两字符串是否相等
        list_num = [x for x in s.lower() if x.isalpha() or x.isdigit()]
        str_1 = str(list_num)
        list_num.reverse()
        str_2 = str(list_num)
        return True if str_1 == str_2 else False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
