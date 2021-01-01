from typing import List
import unittest

'''
Search(set):
    if size of set is 1 and set[0] == item 
        return info on set[0]
    divide the set into parts A and B
    if A is sorted and the item is in the A's range
        return Search(A)
    if B is sorted and the item is in the B's range
        return Search(B)
    if A is not sorted
        return Search(A)
    if B is not sorted
        return Search(B)
    return "not found"
'''
def bsearch(nums: List[int], target: int, i: int, j: int) -> int:
    l, r = i, j
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[l] <= target < nums[m]: # left is sorted
            r = m - 1
        elif nums[m] < target <= nums[r]: # right is sorted
            l = m + 1
        elif nums[m] > nums[r]: # right is not sorted
            l = m + 1
        elif nums[l] > nums[m]: # left is not sorted
            r = m - 1
        else:
            result = bsearch(nums, target, l, m - 1)
            if (result == -1):
                return bsearch(nums, target, m + 1, r)
            else:
                return result
    return -1

def find_k(nums: List[int], target: int) -> int:
    return bsearch(nums, target, 0, len(nums) - 1)

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [3, 4, 5, 1, 2]
        t = 1
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(t, A[result])

    def test_ex2(self):
        A = [3, 4, 5, 1, 2]
        t = 6
        result = find_k(A, t)
        self.assertEqual(-1, result)

    def test_ex3(self):
        A = [0, 1, 2, 3, 4, 5]
        t = 3
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(t, A[result])

    def test_ex4(self):
        A = [1, 3, 1, 1, 1]
        t = 3
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(t, A[result])

    def test_ex5(self):
        A = [1, 3, 1, 1, 1]
        t = 1
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

    def test_ex6(self):
        A = [3, 5, 1]
        t = 3
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

    def test_ex7(self):
        A = [5, 1, 3]
        t = 5
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

    def test_ex8(self):
        A = [5, 1, 3]
        t = 3
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

    def test_ex9(self):
        A = [3, 1]
        t = 1
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

    def test_ex10(self):
        A = [1, 1, 3, 1]
        t = 3
        result = find_k(A, t)
        self.assertNotEqual(-1, result)
        self.assertEqual(A[result], t)

if __name__ == "__main__":
    unittest.main(verbosity=2)
