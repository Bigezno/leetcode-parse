#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  20:18
desc: 杨辉三角
tag:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
            d[n] = 第n行的列表
            n = 0, [1]
            n = 1, [1, 1]
            n = 2, [1, 2, 1]
            n = 3, [1, 3, 3, 1]
            n = 4, [1, 4, 6, 4, 1]
            d[n] = [1, 1 + d[n-1][i]...., 1]
        '''
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[]] * numRows
        result[0] = [1]
        result[1] = [1, 1]
        for i in range(2, numRows):
            item_list = []
            for j in range(i):
                if j == 0:
                    item_list.append(result[i - 1][j])
                    item_list.append(result[i - 1][j] + result[i - 1][j + 1])
                else:
                    if j == i - 1:
                        item_list.append(result[i - 1][j])
                    else:
                        item_list.append(result[i - 1][j] + result[i - 1][j + 1])
            result[i] = item_list
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))