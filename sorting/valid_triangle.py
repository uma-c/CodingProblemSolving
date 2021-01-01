from typing import List
import unittest

def get_number_of_valid_triangles(nums: List[int]) -> int:
    if len(nums) < 3:
        return 0
    ns = sorted(nums)
    count = 0
    for i in range(len(ns) - 2):
        if not ns[i]:
            continue
        k = i + 2
        for j in range(i + 1, len(ns) - 1):
            if not ns[j]:
                continue
            s = ns[i] + ns[j]
            while k < len(ns) and s > ns[k]:
                k += 1
            count += k - j - 1
    return count

class Tests(unittest.TestCase):
    def test_ex1(self):
        result = get_number_of_valid_triangles([2,2,3,4])
        self.assertEqual(3, result)

    def test_ex2(self):
        result = get_number_of_valid_triangles([0,1,0,1])
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)