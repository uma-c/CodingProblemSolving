'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.


Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
from typing import List
import unittest

class LargestNumKey(str):
    def __lt__(x, y):
        print(x, y)
        return x + y > y + x

def largest_number(nums: List[int]) -> str:
    sorted_nums = sorted(map(str, nums), key=LargestNumKey)
    print(sorted_nums)
    ln = ''.join(sorted_nums)
    return ln if ln[0] != '0' else '0'

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual('210', largest_number([10, 2]))

    def test_ex2(self):
        self.assertEqual('9534330', largest_number([3,30,34,5,9]))

if __name__ == "__main__":
    unittest.main(verbosity = 2)