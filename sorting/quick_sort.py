from typing import List
import unittest

# 3 - way partitioning
# ...< p...p p...> p
# equal is partition indexer
def partition(nums: List[int], s:int, e:int) -> int:
    p = nums[e]
    smaller, equal, larger = s, s, e - 1
    while equal <= larger:
        if nums[equal] < p:
            nums[smaller], nums[equal] = nums[equal], nums[smaller] 
            smaller += 1
            equal += 1
        elif nums[equal] == p:
            equal += 1
        else:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1
    nums[equal], nums[e] = nums[e], nums[equal]
    return equal    

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

    def test_quick_select_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = quick_select(nums, 3)
        self.assertEqual(6, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)