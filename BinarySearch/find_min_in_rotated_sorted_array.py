'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array. 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''
from typing import List
import unittest

def find_minimum(nums:List[int])->int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m - 1] > nums[m]:
            return nums[m]
        elif nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1

    return nums[l] if 0 <= l < len(nums) else nums[0]

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(1, find_minimum([3,4,5,1,2]))

    def test_ex2(self):
        self.assertEqual(0, find_minimum([4,5,6,7,0,1,2]))

    def test_ex3(self):
        self.assertEqual(11, find_minimum([11,13,15,17]))

    def test_ex4(self):
        self.assertEqual(1, find_minimum([4, 5, 1, 2, 3]))

if __name__ == "__main__":
    unittest.main(verbosity = 2)