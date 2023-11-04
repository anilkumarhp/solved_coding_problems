#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: Anil kumar H P.
@file: duplicate_zeros.py
@time: 04-11-2023 19:19
@problem_statement: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to
 the right.
@Constraints:
    1 <= arr.length <= 104
    0 <= arr[i] <= 9
"""
from typing import List


class Solution:


    def duplicate_zeros_solution_1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        arr_len = len(arr)
        i = 0
        while i < arr_len - 1:
            if arr[i] == 0:
                # Capture the value
                prev_val = arr[i + 1]

                for j in range(i+2, arr_len):
                    if j < arr_len:
                        # Swap the values
                        arr[j], prev_val = prev_val, arr[j]

                # Duplicate the zero
                arr[i + 1] = 0
                i = i + 2
            else:
                i = i + 1
        print(arr)

    def duplicate_zeros_solution_2(self, arr: list[int]) -> None:

        length = len(arr)
        i = 0

        while i < length:
            if arr[i] == 0:
                # Shift elements to the right
                for j in range(length - 1, i, -1):
                    if j + 1 < length:
                        arr[j + 1] = arr[j]
                # Duplicate the zero
                i += 1
            i += 1
        print(arr)


solution = Solution()
solution.duplicate_zeros_solution_1([1, 0, 2, 3, 0, 4, 5, 0])
solution.duplicate_zeros_solution_2([1, 2, 3])
