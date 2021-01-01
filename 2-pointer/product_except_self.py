from typing import List
import unittest

def get_product_except_self(nums: List[int]) -> List[int]:
    if not nums or len(nums) < 1:
        return nums

    products = [1] * len(nums)
    product = 1
    for i in range(1, len(nums)):
        product *= nums[i - 1]
        products[i] = product        

    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] = right_product * products[i]
        right_product *= nums[i]

    return products

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [1, 2, 4, 16]
        result = get_product_except_self(nums)
        self.assertEqual([128, 64, 32, 8], result)

    def test_ex2(self):
        nums = [2, 3, 4]
        result = get_product_except_self(nums)
        self.assertEqual([12, 8, 6], result)

    def test_ex3(self):
        nums = []
        result = get_product_except_self(nums)
        self.assertEqual([], result)

    def test_ex4(self):
        nums = [2]
        result = get_product_except_self(nums)
        self.assertEqual([1], result)

if __name__ == "__main__":
    unittest.main(verbosity=2)