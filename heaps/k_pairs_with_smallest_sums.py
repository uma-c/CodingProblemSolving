'''
373. Find K Pairs with Smallest Sums
Medium

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''
from typing import List
import heapq

def k_smallest_pairs(nums1:List[int], nums2:List[int], k:int) -> List[List[int]]:
    if not nums1 or not nums2:
        return []
    n1, n2 = len(nums1), len(nums2)
    if k > n1 * n2:
        k = n1 * n2
    l = []
    for i in range(n1):
        for j in range(n2):
            l.append([nums1[i], nums2[j]])
    return heapq.nsmallest(k, l, key = lambda x: x[0] + x[1])

if __name__ == "__main__":
    print(k_smallest_pairs([1,1,2], [1,2,3], 5))