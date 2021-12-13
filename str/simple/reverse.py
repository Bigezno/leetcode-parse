#!/usr/bin/env python
# !-*-coding:utf-8 -*-
'''
Author: peekaboo
date:  18:57
desc: 整数反转
tag: 数学，字符串
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        symbol = -1 if x < 0 else 1
        nums = str(-x) if x < 0 else str(x)
        item_list = []
        for i in reversed(range(0, len(nums))):
            if i == len(nums) - 1 and nums[i] == "0":
                continue
            item_list.append(nums[i])
        print(item_list)
        # 2**31 => 2147483648
        if len(item_list) > 10:
            return 0

        if len(item_list) == 10:
            max_num_list = []
            for num in str(2**31):
                max_num_list.append(num)
            for i in range(0, len(item_list)):
                if i == len(item_list) - 1 and x > 0:
                    if int(item_list[i]) >= int(max_num_list[i]):
                        return 0
                if int(item_list[i]) > int(max_num_list[i]):
                    return 0
                if int(item_list[i]) < int(max_num_list[i]):
                    break

        return symbol * int("".join(item_list))


    def reverse_2(self, x: int) -> int:
        res = 0
        while x!= 0:
            tmp = x % 10
            # 由于不能根据完整数据(因为数据溢出)判断,所以要判断前一位
            if res > 214748364 or (res == 214748364 and tmp > 7):
                return 0
            if res < -214748364 or (res == 214748364 and tmp < -8):
                return 0
            res = res * 10 + tmp
            x = x // 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverse_2(-2147483412))
    # print(2**31)  # 2**31 == 2147483648 -2147483412

