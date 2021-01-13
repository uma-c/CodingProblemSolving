from typing import List
import unittest
from partition import partition

def _quick_select(nums:List[int], k:int, s:int, e:int) -> int:
    if s >= e:
        return nums[s]

    p = partition(nums, s, e)
    if p == k:
        return nums[p]
    elif p > k:
        return _quick_select(nums, k, s, p - 1)
    else:
        return _quick_select(nums, k, p + 1, e)

def quick_select(nums:List[int], k:int) -> int:
    return _quick_select(nums, k, 0, len(nums) - 1)

class Tests(unittest.TestCase):
    def test_quick_select_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = quick_select(nums, 3)
        self.assertEqual(6, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)