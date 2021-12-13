#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  21:19
desc: 实现 strStr()
tag:双指针 字符串 字符串匹配
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。
说明：
当[needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
    输入：haystack = "hello", needle = "ll"
    输出：2

示例 2：
    输入：haystack = "aaaaa", needle = "bba"
    输出：-1

示例 3：
    输入：haystack = "", needle = ""
    输出：0
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        此算法在很多很多个重复字符时会超时
        :param haystack:
        :param needle:
        :return:
        '''
        if needle == "":
            return 0
        left_index = 0
        while left_index < len(haystack):
            left_pointer = left_index
            right_pointer = 0
            # left和right首字符相等，则判断后续是否相等
            if haystack[left_pointer] == needle[right_pointer]:
                while right_pointer < len(needle) and left_pointer < len(haystack): # 要注意当len(haystack) < len(needle)
                    if haystack[left_pointer] != needle[right_pointer]:
                        break
                    left_pointer += 1
                    right_pointer += 1
                if right_pointer == len(needle):
                    return left_index
            left_index += 1
        return -1


    def strStr2(self, haystack: str, needle: str):
        '''
        最佳解法：滑动窗口
        :param haystack:
        :param needle:
        :return:
        '''
        n = len(haystack)
        left = 0
        right = len(needle)
        if right == 0:
            return 0
        while right <= n:
            if haystack[left: right] == needle:
                return left
            left += 1
            right += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi", "issip"))

""
""
