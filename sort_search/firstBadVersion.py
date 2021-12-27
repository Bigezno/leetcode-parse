#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  00:19
desc: 二分查找
tag:
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = left + (right - left) // 2
        while left < right:
            if isBadVersion(mid):
                # 注意这里不能加1，因为这里的mid是找到的确定值
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) // 2
