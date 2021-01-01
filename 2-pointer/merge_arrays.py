'''
10. Merge Arrays
Question​: Given 2 sorted arrays, A and B, where A is long enough to hold the contents of
A and B, write a function to copy the contents of B into A without using any buffer or
additional memory.
eg.
A = {​1​,​3​,​5​,​0​,​0​,​0​}
B = {​2​,​4​,​6​}
mergeArrays(A, B)
A = {​1​,​2​,​3​,​4​,​5​,​6​}
'''
from typing import List
import unittest

def merge(arr1: List[int], target: List[int]):
    m, n = len(arr1), len(target)
    i = m - 1
    j = n - i - 2
    k = n - 1
    while i >= 0 and j >= 0:
        if target[j] > arr1[i]:
            target[k] = target[j]
            j -= 1
        else:
            target[k] = arr1[i]
            i -= 1
        k -= 1

    while i >= 0:
        target[k] = arr1[i]
        k -= 1
        i -= 1
    
    while j >= 0:
        target[k] = target[j]
        k -= 1
        j -= 1

class Tests(unittest.TestCase):
    def test_ex1(self):
        n = 6
        target = [0] * n
        arr1 = [0] * (n // 2)
        j = 0
        expected = [0] * n
        for i in range(1, n + 1):
            expected[i - 1] = i
        for i in range(1, n + 1, 2):
            target[j] = i
            arr1[j] = i + 1
            j += 1

        merge(arr1, target)
        self.assertEqual(expected, target)

    def test_ex2(self):
        A = [-1, 0, 2, 6, 7, 0, 0]
        B = [3, 4]
        merge(B, A)
        self.assertEqual([-1, 0, 2, 3, 4, 6, 7], A)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
