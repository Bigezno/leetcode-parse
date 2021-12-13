#!/usr/bin/env python
#!-*-coding:utf-8 -*-
'''
Author: peekaboo
date: 2021/12/8 19:58
desc: 有效的数独
TAG: 数组 哈希表 矩阵
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

注意：
    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    空白格用 '.' 表示。

示例 2：
    输入：board =
    [["8","3",".", ".","7",".", ".",".","."]
    ,["6",".",".", "1","9","5", ".",".","."]
    ,[".","9","8", ".",".",".", ".","6","."]

    ,["8",".",".", ".","6",".", ".",".","3"]
    ,["4",".",".", "8",".","3", ".",".","1"]
    ,["7",".",".", ".","2",".", ".",".","6"]

    ,[".","6",".", ".",".",".", "2","8","."]
    ,[".",".",".", "4","1","9", ".",".","5"]
    ,[".",".",".", ".","8",".", ".","7","9"]]
    输出：false
    解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

提示：
    board.length == 9
    board[i].length == 9
    board[i][j] 是一位数字（1-9）或者 '.'

解题思路:

'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            line_num_dict = {}
            column_num_dict = {}
            nine_num_dict = {}
            for j in range(0, len(board)):
                if board[j][i] != ".":
                    if board[j][i] in column_num_dict.keys():
                        return False
                    column_num_dict[board[j][i]] = 1

                if board[i][j] != ".":
                    if board[i][j] in line_num_dict.keys():
                        return False
                    line_num_dict[board[i][j]] = 1

                a = (i // 3) * 3 + j // 3
                b = (i % 3) * 3 + j % 3
                if board[a][b] != ".":
                    if board[a][b] in nine_num_dict.keys():
                        return False
                    nine_num_dict[board[a][b]] = 1
        return True
