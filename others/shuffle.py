#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  23:38
desc: 
tag:
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.origin_list = nums


    def reset(self) -> List[int]:
        return self.origin_list


    def shuffle(self) -> List[int]:
        length = len(self.origin_list)
        clone_list = self.origin_list[0:]
        for i in range(length):
            temp = clone_list[i]
            index = randint(i, length - 1)
            clone_list[i] = clone_list[index]
            clone_list[index] = temp
        return clone_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()