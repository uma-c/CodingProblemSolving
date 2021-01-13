'''
4. Find Duplicates
Question​: Given an array of integers where each value 1 <= x <= len(array), write a
function that finds all the duplicates in the array.
eg.
dups([​1​, ​2​, ​3​]) = []
dups([​1​, ​2​, ​2​]) = [​2​]
dups([​3​, ​3​, ​3​]) = [​3​]
dups([​2​, ​1​, ​2​, ​1​]) = [​1​, ​2​]
'''
from typing import List
import unittest

# Time complexity = O(n), Space complexity = O(1)
def find_duplicates(A:List[int]) -> List[int]:
    dups = set()
    for i in range(len(A)):
        index = abs(A[i]) - 1
        if A[index] < 0:
            dups.add(abs(A[i]))
        else:
            A[index] = -A[index]
    return list(dups)

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [1, 2, 3]
        dups = find_duplicates(A)
        self.assertEqual([], dups)

    def test_ex2(self):
        A = [1, 2, 2]
        dups = find_duplicates(A)
        self.assertEqual([2], dups)
    
    def test_ex3(self):
        A = [3, 3, 3]
        dups = find_duplicates(A)
        self.assertEqual([3], dups)

    def test_ex4(self):
        A = [2, 1, 2, 1]
        dups = find_duplicates(A)
        self.assertEqual([1, 2], dups)

    def test_ex5(self):
        A = [10,2,5,10,9,1,1,4,3,7]
        dups = find_duplicates(A)
        self.assertEqual([1, 10], dups)

if __name__ == "__main__":
    unittest.main(verbosity=2)