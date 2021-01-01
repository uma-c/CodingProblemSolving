from typing import List
import unittest

def bubble_sort(nums:List[int]) -> None:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        bubble_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], nums)

if __name__ == "__main__":
    unittest.main(verbosity = 2)