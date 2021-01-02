from typing import List
import unittest

def count_sort(nums:List[int], radix) -> List[int]:
    counter = [0] * 10
    for num in nums:
        key = (num // radix) % 10
        counter[key] += 1

    for i in range(1, 10):
        counter[i] += counter[i-1]

    sorted_nums = [None] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        key = (nums[i] // radix) % 10
        counter[key] -= 1
        sorted_nums[counter[key]] = nums[i]
    return sorted_nums

def radix_sort(nums:List[int]) -> List[int]:
    nums_max = max(nums)
    radix = 1
    while nums_max // radix > 0:
        nums = count_sort(nums, radix)
        radix *= 10
    return nums

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [175, 45, 75, 90, 802, 24]
        result = radix_sort(nums)
        self.assertEqual([24, 45, 75, 90, 175, 802], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)