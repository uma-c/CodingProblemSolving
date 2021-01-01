'''
Given a sorted array nums, 
remove the duplicates in-place such that 
each element appears only once and returns the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

Given a sorted array nums, 
remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List
import unittest

def remove_dups(nums: List[int])->int:    
    ''' 
    two pointers i and j
    [0..i] Uniques
    [i + 1..j] Untouched elements
    [j + 1 ..n) Unprocessed elements
    '''
    if nums is None:
        return None

    if len(nums) < 1:
        return 0
    
    i = j = 0
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = remove_dups(A)
        self.assertEqual(5, result)
        self.assertEqual([0, 1, 2, 3, 4], A[0:result])

    def test_ex2(self):
        A = []
        result = remove_dups(A)
        self.assertEqual(0, result)
        self.assertEqual([], A[0:result])

    def test_ex3(self):
        A = [1, 2, 3]
        result = remove_dups(A)
        self.assertEqual(3, result)
        self.assertEqual([1, 2, 3], A[0:result])

if __name__ == "__main__":
    unittest.main(verbosity = 2)