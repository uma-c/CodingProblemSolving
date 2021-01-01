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
    return l       

class Tests(unittest.TestCase):
    def test_lower_bound_ex1(self):
        A = [1, 3, 4, 4, 4, 4, 5, 6, 7, 8]
        t = 4
        result = lowerbound(A, t)
        lower_bound = bisect_left(A, t)
        #print(lower_bound)
        self.assertEqual(lower_bound, result)

    def test_upper_bound_ex2(self):
        A = [1, 3, 4, 4, 4, 4, 5, 6, 7, 8]
        t = 4
        result = upperbound(A, t)
        upper_bound = bisect_right(A, t)
        #print(upper_bound)
        self.assertEqual(upper_bound, result)

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