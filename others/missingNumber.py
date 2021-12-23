#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  21:19
desc: 缺失数字
tag:
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例：
    输入：nums = [3,0,1]
    输出：2
    解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

提示：
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二
'''
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = range(len(nums) + 1)
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i] ^ all_nums[i]
        return res ^ all_nums[len(nums)]

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))