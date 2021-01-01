'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
'''
from typing import List
import unittest

def longest_continuous_increasing_subseq(nums: List[int]) -> int:
    if len(nums) < 1:
        return 0
    i, max_l, l, n = 1, 1, 1, len(nums)
    while i < n:
        if nums[i - 1] < nums[i]:
            l += 1
        else:
            max_l = max(l, max_l)
            l = 1
        i += 1

    return max(l, max_l)

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(3, longest_continuous_increasing_subseq([1,3,5,4,7]))

    def test_ex2(self):
        self.assertEqual(1, longest_continuous_increasing_subseq([2,2,2,2,2]))

if __name__ == "__main__":
    unittest.main(verbosity = 2)