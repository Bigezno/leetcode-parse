#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:49
desc: 合并两个有序数组
tag: 数组 双指针 排序
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index = 0
        num2_index = 0
        while num1_index < m and num2_index < n:
            if nums1[num1_index] < nums2[num2_index]:
                num1_index += 1
            else:
                nums1.insert(num1_index, nums2[num2_index])
                num2_index += 1
                num1_index += 1
                m += 1
                # 将补0的元素给剔除
                nums1.pop()
        while num2_index < n:
            nums1[num1_index] = nums2[num2_index]
            num2_index += 1
            num1_index += 1


if __name__ == '__main__':
    s = Solution()
    node = []
    node.pop()
