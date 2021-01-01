from typing import List
import unittest
'''
eliminate elements from both arrays by checking median of the arrays
'''
class SubArray(object):
    def __init__(self, A:List[int], start:int, n:int):
        self.arr = A
        self.set(start, n)
    
    def set(self, start, n):
        if 0 <= start < len(self.arr):
            self.start = start
            self.size = n if (start + n - 1) < len(self.arr) else (len(self.arr) - start)
        else:
            raise ValueError("Invalid input")


def median_of_subarray(A:SubArray):
    mid = A.start + (A.size - 1) // 2
    if A.size % 2 == 0: # even number of elements
        return (A.arr[mid] + A.arr[mid + 1]) / 2
    else: # odd number of elements
        return A.arr[mid]

def merge_subarrays(A:SubArray, B:SubArray) -> List[int]:
    temp = []
    a, b = A.start, B.start
    a_end, b_end = a + A.size - 1, b + B.size - 1
    while a <= a_end and b <= b_end:
        if A.arr[a] <= B.arr[b]:
            temp.append(A.arr[a])
            a += 1
        else:
            temp.append(B.arr[b])
            b += 1
        
    while a <= a_end:
        temp.append(A.arr[a])
        a += 1

    while b <= b_end:
        temp.append(B.arr[b])
        b += 1
        
    return temp    

def median_of_subarrays(A:SubArray, B:SubArray) -> int:
    if (A.size + B.size) < 5:
        temp = merge_subarrays(A, B)
        return median_of_subarray(SubArray(temp, 0, len(temp)))
    
    m_A = median_of_subarray(A)
    m_B = median_of_subarray(B)
    if m_A == m_B:
        return m_A
    else:
        if m_A < m_B:
            mid_A = A.start + A.size // 2
            A.set(mid_A, A.size // 2 + 1)
            B.set(B.start, B.size // 2 + 1)
        else:
            mid_B = B.start + B.size // 2
            A.set(A.start, A.size // 2 + 1)
            B.set(mid_B, B.size // 2 + 1)
        return median_of_subarrays(A, B)

def median(A:List[int], B:List[int]) -> int:
    if len(A) > 0 and len(B) > 0:
        return median_of_subarrays(SubArray(A, 0, len(A)), SubArray(B, 0, len(B)))
    elif len(A) > 0:
        return median_of_subarray(SubArray(A, 0, len(A)))
    elif len(B) > 0:
        return median_of_subarray(SubArray(B, 0, len(B)))
    else:
        raise ValueError("invalid input")

class Tests(unittest.TestCase):
    # def test_ex1(self):
    #     A = [1, 3, 5]
    #     B = [2, 4, 6]
    #     m = median(A, B)
    #     self.assertEqual(3.5, m)

    # def test_ex2(self):
    #     A = []
    #     B = [1, 2, 3]
    #     m = median(A, B)
    #     self.assertEqual(2, m)

    # def test_ex3(self):
    #     A = [1, 2, 3, 4]
    #     B = []
    #     m = median(A, B)
    #     self.assertEqual(2.5, m)

    def test_ex4(self):
        B = [3, 4]
        A = [1, 2, 5, 6, 7]
        m = median(A, B)
        self.assertEqual(4, m)

    # def test_median_subarray_ex1(self):
    #     A = [1, 2, 3, 4]
    #     m = median_of_subarray(SubArray(A, 0, len(A)))
    #     self.assertEqual(2.5, m)

    # def test_median_subarray_ex2(self):
    #     A = [1, 2, 3, 4, 5]
    #     m = median_of_subarray(SubArray(A, 0, len(A)))
    #     self.assertEqual(3, m)

    # def test_median_subarray_ex3(self):
    #     A = [1, 2, 3, 4]
    #     m = median_of_subarray(SubArray(A, 1, 3))
    #     self.assertEqual(3, m)

    # def test_merge_subarrays(self):
    #     A = [1, 2, 3]
    #     B = [4, 5, 6]
    #     C = merge_subarrays(SubArray(A, 1, 2), SubArray(B, 0, 2))
    #     self.assertEqual([2, 3, 4, 5], C)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # B = [3, 4]
    # A = [1, 2, 5, 6, 7]
    # # temp = merge_subarrays(SubArray(A, 0, len(A) - 1), SubArray(B, 0, len(B) - 1))
    # # m = median_of_subarray(SubArray(temp, 0, len(temp) - 1))
    # m = median(A, B)
    # print(m)