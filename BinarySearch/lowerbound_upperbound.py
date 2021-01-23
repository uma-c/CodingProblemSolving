import unittest
from typing import List
from bisect import bisect_left, bisect_right

# move towards left
def lowerbound(A: List[int], t:int) -> int:
    l, r = 0, len(A) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] >= t:
            r = mid - 1
        else:
            l = mid + 1
    if not (0 <= l < len(A)) or A[l] != t:
        return -1
    return l

# move towards right
def upperbound(A: List[int], t:int) -> int:
    l, r = 0, len(A) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] <= t:
            l = mid + 1
        else:
            r = mid - 1
    if not (0 <= r < len(A)) or A[r] != t:
        return -1
    return r    

class Tests(unittest.TestCase):
    def test_lower_bound_ex1(self):
        A = [1, 3, 4, 4, 4, 4, 5, 6, 7, 8]
        t = 4
        result = lowerbound(A, t)
        lower_bound = bisect_left(A, t)
        #print(lower_bound)
        self.assertEqual(lower_bound, result)

    def test_lowerbound_ex2(self):
        A = [1,1,2,2,2,2,3,3,3]
        self.assertEqual(2, lowerbound(A, 2))

    def test_upperbound_ex1(self):
        A = [1,1,2,2,2,2,3,3,3]
        self.assertEqual(5, upperbound(A, 2))

    def test_upper_bound_ex2(self):
        A = [1, 3, 4, 4, 4, 4, 5, 6, 7, 8]
        t = 4
        result = upperbound(A, t)
        self.assertEqual(5, result)

    def test_upper_bound_ex3(self):
        A = [4, 5, 6, 7, 8]
        t = 6
        result = lowerbound(A, t)
        #print(result)
        upper_bound = bisect_left(A, t)
        #print(upper_bound)
        self.assertEqual(upper_bound, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)