from typing import List
import unittest
from insertion_sort import insertion_sort
from functools import reduce

def bucket_sort(nums:List[int]) -> None:
    if nums is None or len(nums) < 1:
        return
    nums_min = float("inf")
    nums_max = float("-inf")
    n = len(nums)
    for num in nums:
        if num < nums_min:
            nums_min = num
        if num > nums_max:
            nums_max = num

    buckets = [[] for _ in range(n+1)]
    nums_range_factor = n / (nums_max - nums_min)
    for num in nums:
        buckets[int((num - nums_min) * nums_range_factor)].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    return reduce(lambda a, b: a+b, buckets)

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = bucket_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], result)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = bucket_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

    def test_ex3(self):
        nums = [5, -1, 2, 5, 6, 2, -3, -4, 5, 6]
        result = bucket_sort(nums)
        self.assertEqual([-4, -3, -1, 2, 2, 5, 5, 5, 6, 6], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)