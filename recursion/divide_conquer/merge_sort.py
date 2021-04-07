'''
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''
from typing import List

def sortArray(nums: List[int]) -> List[int]:
    def merge(l1: List[int], l2: List[int]) -> List[int]:
        result = []
        c1 = c2 = 0
        n1, n2 = len(l1), len(l2)
        while c1 < n1 and c2 < n2:
            if l1[c1] <= l2[c2]:
                result.append(l1[c1])
                c1 += 1
            else:
                result.append(l2[c2])
                c2 += 1
        result.extend(l1[c1:])
        result.extend(l2[c2:])
        return result
    def sort(nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        l1 = sort(nums[:m])
        l2 = sort(nums[m:])
        return merge(l1, l2)
    return sort(nums)

if __name__ == "__main__":
    nums = [5, 8, 2, 3, 1, 7, 9, 4, 6]
    print(sortArray(nums))