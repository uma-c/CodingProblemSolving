from typing import List
import unittest

def smallest_subarray_sum_gte_k(nums: List[int], s: int)->int:
    if nums is None or len(nums) < 1:
        return 0 
    i = j = 0
    min_window_size = float("inf")
    current_sum = 0
    n = len(nums)
    while j < n:
        current_sum += nums[j]
        while current_sum >= s:
            min_window_size = min(min_window_size, j - i + 1)
            current_sum -= nums[i]
            i += 1
        j += 1

    return min_window_size if min_window_size != float("inf") else 0

class Tests(unittest.TestCase):
    def test_smallest_sum_exists(self):
        arr = [4, 2, 2, 7, 8, 1, 7, 5, 2, 0]
        result = smallest_subarray_sum_gte_k(arr, 8)
        self.assertEqual(result, 1)

    def test_smallest_sum_not_exist(self):
        arr = [1, 1, 1, 1]
        result = smallest_subarray_sum_gte_k(arr, 8)
        self.assertEqual(0, result)


unittest.main(verbosity=2)