#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 19:34
desc: 移动零
TAG: 数组 双指针
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

解题思路:
    初始化: left=0,right=1;
        right > left时：
            a. 如果left的值==0，则将值交换，right右移，left左移；
            b. 否则right右移；
        否则，当left的值!=
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(1, len(nums)):
            if nums[right] and nums[left] == 0:
                nums[left] = nums[right]
                nums[right] = 0
            if nums[left] != 0:
                left += 1


if __name__ == '__main__':
    s = Solution()
    nums = [45192, 0, -659, -52359, -99225, -75991, 0, -15155, 27382, 59818, 0, -30645, -17025, 81209, 887, 64648]
    s.moveZeroes(nums)
    print(nums)
