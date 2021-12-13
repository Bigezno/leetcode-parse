#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 20:56
desc: 旋转图像
TAG: 数组 数学 矩阵
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

提示：
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

解题思路：
    一层一层进行交换
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # 先上下交换
        for i in range(0, length // 2):
            temp = matrix[i]
            matrix[i] = matrix[length - i - 1]
            matrix[length - i - 1] = temp
        # 在按照对角线交换
        for i in range(0, length):
            for j in range(i + 1, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp