'''
5. Consecutive Array
Question​: Given an unsorted array, find the length of the longest sequence of
consecutive numbers in the array.
eg.
consecutive([​4​, ​2​, ​1​, ​6​, ​5​]) = ​3​, [​4​, ​5​, ​6​]
consecutive([​5​, ​5​, ​3​, ​1​]) = ​1​, [​1​], [​3​], or [​5​]
'''
from typing import List
import unittest

# Time Complexity: O(n log n), Space complexity: O(1) assumption is use of quick sort
def max_no_of_consecutive_elements1(A:List[int]) -> int:
    if A is None or len(A) < 1:
        return 0
    sorted_A = sorted(A)
    j = 1
    max_len = 1
    length = 1
    while j < len(sorted_A):
        if sorted_A[j - 1] + 1 == sorted_A[j]:
            length += 1
        else:            
            max_len = max(max_len, length)
            length = 1
        j += 1
    return max(max_len, length)

# Time Complexity: O(n), Space complexity: O(n)
def max_no_of_consecutive_elements(A:List[int]) -> int:
    if A is None or len(A) < 1:
        return 0
    counter = set()
    for num in A:
        counter.add(num)

    length = 1
    max_length = 1
    for num in counter:
        if (num - 1) in counter:
            length += 1
        else:
            max_length = max(max_length, length)
            length = 1
    return max(max_length, length)

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [4, 2, 1, 6, 5]
        result = max_no_of_consecutive_elements(A)
        self.assertEqual(3, result)

    def test_ex2(self):
        A = [5, 5, 3, 1]
        result = max_no_of_consecutive_elements(A)
        self.assertEqual(1, result)

    def test_ex3(self):
        A = [5, 4, 3, 2, 1]
        result = max_no_of_consecutive_elements(A)
        self.assertEqual(5, result)
    
    def test_ex4(self):
        A = []
        result = max_no_of_consecutive_elements(A)
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
