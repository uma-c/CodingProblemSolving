from typing import List
import unittest

def insertion_sort(nums:List[int]) -> None:
    for i in range(len(nums)):
        j = i - 1
        num = nums[i]
        while j >= 0 and num < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = num

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        insertion_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], nums)

if __name__ == "__main__":
    unittest.main(verbosity = 2)