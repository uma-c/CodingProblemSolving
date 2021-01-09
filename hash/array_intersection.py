'''
349. Intersection of Two Arrays
Easy

1159

1411

Add to List

Share
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''
from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums_set = None
    nums = None
    if len(nums1) > len(nums2):
        nums_set = set(nums2)
        nums = nums1
    else:
        nums_set = set(nums1)
        nums = nums2
    result = []
    for num in nums:
        if num in nums_set:
            result.append(num)
            nums_set.remove(num)
    return result