#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  21:07
desc: 有效的括号
tag:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
提示：
    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成
'''

class Solution:
    def isValid(self, s: str) -> bool:
        item = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                item.append(s[i])
                continue
            if s[i] in [')', ']', '}'] and not item:
                return False
            if s[i] == ')' and item.pop() != '(':
                return False
            if s[i] == ']' and item.pop() != '[':
                    return False
            if s[i] == '}' and item.pop() != '{':
                return False
        if item:
            return False
        return True


if __name__ == '__main__':
    item = [1, 2, 3]
    print(item.pop())
    print(item.pop())
    print(item.pop())