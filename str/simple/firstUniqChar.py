#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  20:13
desc: 字符串中的第一个唯一字符
tag: 队列 哈希表 字符串 计数
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
    s = "leetcode"
    返回 0
    s = "loveleetcode"
    返回 2
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        item_dict = {}
        for num in s:
            if num not in item_dict.keys():
                item_dict[num] = 0
            item_dict[num] += 1
        for num in s:
            if item_dict[num] == 1:
                return s.find(num)
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("aabb"))

