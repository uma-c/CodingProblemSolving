from typing import List
import heapq
import unittest

def heap_sort(nums:List[int]) -> List[int]:
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = heap_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], result)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = heap_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)