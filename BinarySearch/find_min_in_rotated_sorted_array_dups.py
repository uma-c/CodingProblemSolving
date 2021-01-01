'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

from typing import List
import unittest

def find_minimum_(nums:List[int], i: int, j: int)->int:
    l, r = i, j
    while l <= r:
        m = l + (r - l) // 2
        if nums[m - 1] > nums[m]:
            return nums[m]
        elif nums[m] > nums[r]:
            l = m + 1
        elif nums[l] > nums[m]:
            r = m - 1
        else:
            return min(find_minimum_(nums, l, m - 1), find_minimum_(nums, m + 1, r) if (m + 1) < len(nums) else float("inf"))

    return nums[l] if 0 <= i <= l <= j < len(nums) else nums[i]

def find_minimum(nums:List[int])->int:
    return find_minimum_(nums, 0, len(nums) - 1)

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(1, find_minimum([3,4,5,1,2]))

    def test_ex2(self):
        self.assertEqual(0, find_minimum([4,5,6,7,0,1,2]))

    def test_ex3(self):
        self.assertEqual(11, find_minimum([11,13,15,17]))

    def test_ex4(self):
        self.assertEqual(1, find_minimum([4, 5, 1, 2, 3]))

    def test_ex5(self):
        self.assertEqual(0, find_minimum([2,2,2,0,1]))
    
    def test_ex6(self):
        self.assertEqual(1, find_minimum([1, 3, 5]))

if __name__ == "__main__":
    unittest.main(verbosity = 2)