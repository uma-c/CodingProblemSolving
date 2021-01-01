'''
363. Max Sum of Rectangle No Larger Than K
Hard

974

73

Add to List

Share
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/665160/Java-TreeSet-solution-with-(m-*-m-*-nlog(n))-Time
https://www.youtube.com/watch?v=gD4dzeQ6YH0
'''
from typing import List
import bisect
import unittest

def upperbound(A: List[int], t:int) -> int:
    l, r = 0, len(A) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] == t:
            return mid
        elif A[mid] < t:
            l = mid + 1
        else:
            r = mid - 1
    return l 

def presum(pre_sums:List[int], matrix: List[List[int]], i: int, is_row: bool = True):
    if is_row:
        for c in range(len(matrix[i])):
            pre_sums[c] += matrix[i][c]
    else:
        for r in range(len(matrix)):
            pre_sums[r] += matrix[r][i]

def max_submatrix_sum(pre_sums:List[int], sorted_sums: List[int], k: int) -> int:
    prefix_sum = 0
    bisect.insort(sorted_sums, prefix_sum)
    max_ceil_val = float("-inf")
    for pre_sum in pre_sums:
        prefix_sum += pre_sum
        ceil = prefix_sum - k
        ceil_val_idx = upperbound(sorted_sums, ceil)
        ceil_val = sorted_sums[ceil_val_idx] if 0 <= ceil_val_idx < len(sorted_sums) else float("inf")
        if ceil_val == ceil:
            return k
        else:
            max_ceil_val = max(max_ceil_val, prefix_sum - ceil_val)   
        bisect.insort(sorted_sums, prefix_sum)
    return max_ceil_val

def max_sum_of_rect_no_larger_than_k(matrix:List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])
    max_ceil = float("-inf")
    if m <= n:
        for i in range(m):
            pre_sums = [0] * n
            for j in range(i, m):
                presum(pre_sums, matrix, j)
                sorted_sums = []
                max_ceil = max(max_ceil, max_submatrix_sum(pre_sums, sorted_sums, k))
                if max_ceil == k:
                    return k
    else:
        for i in range(n):
            pre_sums = [0] * m
            for j in range(i, n):
                presum(pre_sums, matrix, j, False)
                sorted_sums = []
                max_ceil = max(max_ceil, max_submatrix_sum(pre_sums, sorted_sums, k))
                if max_ceil == k:
                    return k
    return max_ceil if max_ceil != float("-inf") else -1

class Tests(unittest.TestCase):
    def test_ex1(self):
        matrix = [[1,0,1],[0,-2,3]]
        k = 2
        self.assertEqual(2, max_sum_of_rect_no_larger_than_k(matrix, k))

    def test_ex2(self):
        matrix = [[2, 2, -1]]
        k = 0
        self.assertEqual(-1, max_sum_of_rect_no_larger_than_k(matrix, k))

    def test_ex3(self):
        matrix = [[2, 2, -1]]
        k = 3
        self.assertEqual(3, max_sum_of_rect_no_larger_than_k(matrix, k))

    def test_ex4(self):
        matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
        k = 10
        self.assertEqual(10, max_sum_of_rect_no_larger_than_k(matrix, k))

    def test_ex5(self):
        matrix = [[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
        k = -100
        self.assertEqual(-101, max_sum_of_rect_no_larger_than_k(matrix, k))

    def test_ex6(self):  
        matrix = [[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]]
        k = 12
        self.assertEqual(12, max_sum_of_rect_no_larger_than_k(matrix, k))

if __name__ == "__main__":
    unittest.main(verbosity = 2)