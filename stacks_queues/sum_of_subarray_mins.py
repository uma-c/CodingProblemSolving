'''
907. Sum of Subarray Minimums
Medium

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000


Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
'''
from typing import List

def sum_of_subarray_mins(nums:List[int]) -> int:
    s = []
    ans = 0
    A = [0] + nums + [0]
    for i, val in enumerate(A):
        while s and val < A[s[-1]]:
            j = s.pop()
            k = s[-1]
            ans += A[j] * (i - j) * (j - k)
        s.append(i)
    return ans % (10**9 + 7)

if __name__ == "__main__":
    print(sum_of_subarray_mins([3,1,2,4]))
    print(sum_of_subarray_mins([11,81,94,43,3]))