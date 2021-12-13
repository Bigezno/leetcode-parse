#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  22:21
desc: 外观数列
tag:字符串
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
'''

class Solution:
    # 递归 + 双指针
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        # 获取上次的值
        last_str = self.countAndSay(n-1)
        item_list = []
        left = 0
        right = 0
        while left < len(last_str) and right < len(last_str):
            if last_str[left] == last_str[right]:
                right += 1
            else:
                item_list.append("{}{}".format(right-left, last_str[left]))
                left = right
        item_list.append("{}{}".format(right-left, last_str[left]))
        return "".join(item_list)


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))