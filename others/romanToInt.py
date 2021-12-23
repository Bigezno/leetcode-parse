#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  17:33
desc: 罗马数字转整形
tag:
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        # 把所有的字符列出来，每次截取两个字符，如果这两个字符能够代表一个独立数就保留，否则就截取一个字符
        chars_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        num = 0
        i = 0
        while i < len(s):
            chars = s[i:i+2]
            if chars in chars_dict.keys():
                i += 2
            else:
                chars = s[i:i+1]
                i += 1
            num += chars_dict[chars]
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
