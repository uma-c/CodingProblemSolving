'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

from typing import List
import sys
import unittest

sys.path.append('C:\Repos\CodingProblemSolving\sorting')
from partition import partition, partition_reverse

def _quick_select(nums:List[int], k:int, s:int, e:int, reverse: bool = False) -> int:
    pf = partition_reverse if reverse else partition
    while s <= e:
        p = pf(nums, s, e)
        if p == k:
            return nums[p]
        elif p > k:
            e = p - 1
        else:
            s = p + 1
    return nums[s]

def find_kth_largest(nums: List[int], k:int) -> int:
    n = len(nums)
    if k < n // 2:
        return _quick_select(nums, k - 1, 0, n - 1, k < n // 2) # 0 based index, k is 1..n
    else:
        return _quick_select(nums, n - k, 0, n - 1, k < n // 2) # 0 based index, k is 1..n

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [3,2,1,5,6,4]
        result = find_kth_largest(nums, 2)
        self.assertEqual(5, result)

    def test_ex2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        result = find_kth_largest(nums, 4)
        self.assertEqual(4, result) 

    def test_ex3(self):
        nums = [2,3,1,4,5,5,6]
        result = find_kth_largest(nums, 4)
        self.assertEqual(4, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)