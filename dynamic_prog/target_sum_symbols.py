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

Solution
--------
sum(p) - sum(n) = target_sum
sum(p) - sum(n) + sum(nums) = target_sum + sum(nums)
sum(p) - sum(n) + sum(p) + sum(n) = target_sum + sum(nums)
2 * sum(p) = target_sum + sum(nums)
sum(p) = (target_sum + sum(nums)) / 2
'''

import unittest
from typing import List

def find_target_sum_ways(nums: List[int], t: int) -> int:
    s = sum(nums) # O(n)
    ps = (t + s) // 2 # positives sum
    if t > s or -t < -s or ps != ((t + s) / 2):
        return 0
    prev_row = [0] * (ps + 1)
    prev_row[0] = 1
    curr_row = None
    for num in nums:
        curr_row = [0] * (ps + 1)
        for j in range(0, ps + 1):
            if num > j:
                curr_row[j] = prev_row[j]
            else:
                curr_row[j] = prev_row[j] + prev_row[j - num] # without curr num + with curr num
        prev_row = curr_row
    return curr_row[ps] if curr_row is not None else 0

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