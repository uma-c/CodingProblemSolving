from typing import List
import unittest

# top down
def largest_sum_non_adjacent_nums_(nums: List[int], cache: List[int], i: int) -> int:
    if i < 0 or i >= len(nums):
        return 0

    if not cache[i] is None:
        return cache[i]

    cache[i] = max(nums[i] + largest_sum_non_adjacent_nums_(nums, cache, i + 2), largest_sum_non_adjacent_nums_(nums, cache, i + 1))
    return cache[i]

# bottom up
def largest_sum_non_adjacent_nums_bu(nums: List[int]) -> int:
    if nums is None or len(nums) < 1:
        return 0
    if len(nums) < 3:
        return max(nums)
    a = nums[0]
    b = max(nums[0], nums[1])
    max_sum = b
    for i in range(2, len(nums)):
        c = max(nums[i] + a, b)
        max_sum = max(c, max_sum)
        a, b = b, c    
    return max_sum

def largest_sum_non_adjacent_nums(nums: List[int]) -> int:
    cache = [None] * len(nums)
    return largest_sum_non_adjacent_nums_(nums, cache, 0)

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [2, 4, 6, 2, 5] 
        self.assertEqual(13, largest_sum_non_adjacent_nums(nums))

    def test_ex2(self):
        nums = [5, 1, 1, 5] 
        self.assertEqual(10, largest_sum_non_adjacent_nums(nums))

if __name__ == "__main__":
    unittest.main(verbosity=2)