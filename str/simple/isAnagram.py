#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  20:32
desc: 有效的字母异位词
tag: 哈希表 字符串 排序

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first_dict = {}
        for n in s:
            if n not in first_dict.keys():
                first_dict[n] = 0
            first_dict[n] += 1

        second_dict = {}
        for i in t:
            if i not in second_dict.keys():
                second_dict[i] = 0
            second_dict[i] += 1

        for key in first_dict.keys():
            if key not in second_dict or first_dict[key] != second_dict[key]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s="anagraam", t="nagaram"))
