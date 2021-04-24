'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6
 

Follow up: The overall run time complexity should be O(log (m+n)).
'''
from typing import List

'''
https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
'''
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def median(A: List[int]):
        m = -(-len(A) // 2)
        if len(A) % 2 == 0:
            return (A[m] + A[m - 1]) / 2
        return A[m - 1]
    def median_of_two(A: List[int], B: List[int]):
        m, n = len(A), len(B)
        if m > n:
            return median_of_two(B, A)
        if m > 0:
            i, j, half_len = 0, m, (m + n + 1) // 2
            while i <= j:
                a_c = i + (j - i) // 2
                b_c = half_len - a_c
                if a_c < m and B[b_c - 1] > A[a_c]:
                    i = a_c + 1
                elif a_c > 0 and A[a_c - 1] > B[b_c]:
                    j = a_c - 1
                else:
                    if a_c == 0:
                        max_left = B[b_c - 1]
                    elif b_c == 0:
                        max_left = A[a_c - 1]
                    else:
                        max_left = max(A[a_c - 1], B[b_c - 1])
                    
                    if (m + n) % 2 == 1:
                        return max_left
                    
                    if a_c == m:
                        min_right = B[b_c]
                    elif b_c == n:
                        min_right = A[a_c]
                    else:
                        min_right = min(A[a_c], B[b_c])
                    
                    return (max_left + min_right) / 2.0
        return median(B)    
    return median_of_two(nums1, nums2)

if __name__ == "__main__":
    A = []
    B = [1, 1, 2, 3, 4]
    print(findMedianSortedArrays(A, B))