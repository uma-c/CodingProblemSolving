from typing import List
import unittest

def merge(l: List[int], r:List[int]) -> List[int]:
    result = []
    li, ri = 0, 0
    while li < len(l) and ri < len(r):
        if r[ri] < l[li]:
            result.append(r[ri])
            ri += 1
        else:
            result.append(l[li])
            li += 1
    while li < len(l):
        result.append(l[li])
        li += 1
    while ri < len(r):
        result.append(r[ri])
        ri += 1
    return result

def _merge_sort(nums:List[int], si: int, ei: int) -> List[int]:
    if si == ei:
        return [nums[si]]

    m = si + (ei - si) // 2
    l = _merge_sort(nums, si, m)
    r = _merge_sort(nums, m + 1, ei)
    return merge(l, r)

def merge_sort(nums:List[int]) -> List[int]:
    return _merge_sort(nums, 0, len(nums) - 1)

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [9, 10, 2, 4, 5, 10, 6, 9]
        result = merge_sort(nums)
        self.assertEqual([2, 4, 5, 6, 9, 9, 10, 10], result)

    def test_ex2(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = merge_sort(nums)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)