from typing import List
import unittest

def selection_sort(nums:List[int]) -> None:
    for i in range(len(nums)):
        si = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[si]:
                si = j
        if nums[si] != nums[i]:
            nums[si], nums[i] = nums[i], nums[si]

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        selection_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], nums)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        selection_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], nums)

if __name__ == "__main__":
    unittest.main(verbosity = 2)