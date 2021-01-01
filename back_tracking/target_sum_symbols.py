'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Constraints:
-----------

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

import unittest
from typing import List, Dict

def find_target_sum_ways_backtrack(nums: List[int], t: int, i: int, cache: Dict[int, Dict[int, int]]) -> int:
    if i == len(nums):
        if t == 0:
            return 1
        else:
            return 0

    if cache[i].get(t + 2000):
        return cache[i][t + 2000]

    pos_ways = find_target_sum_ways_backtrack(nums, t - nums[i], i + 1, cache)
    neg_ways = find_target_sum_ways_backtrack(nums, t + nums[i], i + 1, cache)
    cache[i][t + 2000] = pos_ways + neg_ways
    return (pos_ways + neg_ways)

def find_target_sum_ways(nums: List[int], t: int) -> int:
    cache = dict()
    for i in range(len(nums)):
        cache[i] = dict()
    return find_target_sum_ways_backtrack(nums, t, 0, cache)

class Tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_target_sum_ways([1], 1), 1)

    def test_example2(self):
        self.assertEqual(find_target_sum_ways([1,1], 0), 2)

    def test_example3(self):
        self.assertEqual(find_target_sum_ways([1,1,1,1,1], 3), 5)

    def test_example4(self):
        self.assertEqual(find_target_sum_ways([9,7,0,3,9,8,6,5,7,6], 2), 40)

    def test_example5(self):
        self.assertEqual(find_target_sum_ways([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 1000), 0)
    
    def test_example6(self):
        self.assertEqual(find_target_sum_ways([40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15], 3), 7050)

    def test_example7(self):
        self.assertEqual(find_target_sum_ways([46,49,5,7,5,21,27,4,4,27,45,24,7,22,25,5,38,14,50,28], 45), 6273)

    def test_example8(self):
        self.assertEqual(find_target_sum_ways([17,2,1,20,17,36,6,47,5,23,19,9,4,26,46,41,12,11,12,8], 26), 7664)

    def test_example9(self):
        self.assertEqual(find_target_sum_ways([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 2147483647), 0)

    def test_example10(self):
        self.assertEqual(find_target_sum_ways([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 333), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)