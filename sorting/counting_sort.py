from typing import List
import unittest

def counting_sort(nums:List[int]) -> None:
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
    nums_range = nums_max - nums_min
    counter = [0 for _ in range(nums_range+1)]
    for num in nums:
        counter[num - nums_min] += 1
    
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    result = [None for _ in range(n)]
    for i in range(n-1, -1, -1):
        key = nums[i] - nums_min
        counter[key] -= 1
        result[counter[key]] = nums[i]
    return result

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = counting_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], result)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = counting_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)