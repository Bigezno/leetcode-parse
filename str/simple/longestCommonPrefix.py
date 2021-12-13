#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  22:45
desc: 最长公共前缀
tag:字符串
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"

示例 2：
    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 找出最短字符串作为遍历依据
        min_len_str = strs[0]
        min_len = len(strs[0])
        for str_item in strs:
            if len(str_item) < min_len:
                min_len = len(str_item)
                min_len_str = str_item
        item_list = []
        for i in range(min_len):
            flag = min_len_str[i]
            for str_item in strs:
                if flag != str_item[i]:
                    return "".join(item_list)
            item_list.append(flag)
        return "".join(item_list)


if __name__ == '__main__':
    pass