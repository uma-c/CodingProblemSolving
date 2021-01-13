# 3 pointer sliding window
'''
930. Binary Subarrays With Sum. In an array A of 0s and 1s,
how many non-empty subarrays have sum S?
Example 1 :
Input : A = [ 1 , 0 , 1 , 0 , 1 ] , S = 2
Output : 4
Example 2 :
Input : A = [ 1 , 0 , 1 , 0 ] , S = 1
Output : 6
'''

from typing import List
import unittest
import collections

'''
Prefix sum approach
'''
# Time complexity: O(n), Space complexity: O(n)
def no_of_non_empty_subarrays_sum(A: List[int], S: int)->int:
    if A is None or len(A) < 1:
        return 0
    ns = 0
    n = len(A)
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + A[i]

    counter = collections.Counter()
    for p in ps:
        ns += counter[p]
        counter[p + S] += 1
    return ns

'''
3 pointer approach
'''    
# Time complexity: O(n), Space complexity: O(1)
def no_of_non_empty_subarrays_sum1(A: List[int], S: int)->int:
    if A is None or len(A) < 1:
        return 0
    n = len(A)
    ns = 0
    i_hi = i_lo = j = 0
    sum_window = 0
    while j < n:
        sum_window += A[j]
        while i_lo < j and sum_window > S:
            sum_window -= A[i_lo]
            i_lo += 1
        i_hi = i_lo
        while i_hi < j and sum_window == S and not A[i_hi]:
            i_hi += 1        
        if sum_window == S:
            ns += i_hi - i_lo + 1
        j += 1
    return ns
    
class Tests(unittest.TestCase):
    def test_example1(self):
        result = no_of_non_empty_subarrays_sum([1, 0, 1, 0, 1], 2)
        self.assertEqual(4, result)

    def test_example2(self):
        result = no_of_non_empty_subarrays_sum([1, 0, 1, 0], 1)
        self.assertEqual(6, result)

    def test_example3(self):
        result = no_of_non_empty_subarrays_sum([1, 0, 1, 1, 0], 1)
        self.assertEqual(6, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)