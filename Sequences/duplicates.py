from typing import List
import unittest

def get_duplicates(nums:List[int]) -> List[int]:
    if nums is None or len(nums) < 1:
        return nums

    num_set = set()
    dups = set()
    for num in nums:
        if num in num_set:
            dups.add(num)
        else:
            num_set.add(num)

    return list(dups)

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [2, 1, 5, 1, 4, 5, 2, 2, 3]
        self.assertEqual([1, 2, 5], get_duplicates(nums))

if __name__ == "__main__":
    unittest.main(verbosity = 2)