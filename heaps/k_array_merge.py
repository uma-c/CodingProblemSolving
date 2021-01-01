'''
8. Merge K Arrays
Question​: Given k sorted arrays, merge them into a single sorted array.
eg.
merge({{​1​, ​4​, ​7​},{​2​, ​5​, ​8​},{​3​, ​6​, ​9​}}) = {​1​, ​2​, ​3​, ​4​, ​5​, ​6​, ​7​, ​8​, ​9​}
'''
from typing import List
import unittest
from queue import PriorityQueue

def merge(arrays: List[List[int]]) -> List[int]:
    aidx = [0] * len(arrays)
    pq = PriorityQueue()
    for i in range(len(arrays)):
        arr = arrays[i]
        if len(arr) > 0:
            pq.put((arr[0], i))

    result = []
    while not pq.empty():
        e, eidx = pq.get()
        result.append(e)
        if aidx[eidx] < len(arrays[eidx]) - 1:
            aidx[eidx] += 1
            pq.put((arrays[eidx][aidx[eidx]], eidx))

    return result

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [1, 4, 7]
        B = [2, 5, 8]
        C = [3, 6, 9]
        result = merge([A, B, C])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], result)

    def test_ex2(self):
        A = [3, 4, 5]
        B = []
        C = [1, 2, 6, 7]
        result = merge([A, B, C])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], result)

    def test_ex3(self):
        A = []
        B = []
        C = []
        result = merge([A, B, C])
        self.assertEqual([], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)