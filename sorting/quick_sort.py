from typing import List
import unittest
from partition import partition
 
def _quick_sort(nums:List[int], s:int, e:int) -> None:
    if s >= e:
        return
    p = partition(nums, s, e)
    _quick_sort(nums, s, p - 1)
    _quick_sort(nums, p + 1, e)

def quick_sort(nums:List[int]) -> None:
    _quick_sort(nums, 0, len(nums) - 1)

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
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        quick_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], nums)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        quick_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], nums)

if __name__ == "__main__":
    unittest.main(verbosity = 2)