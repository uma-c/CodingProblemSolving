'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def lsearch(i: int, j: int) -> int:
        while (i + 1) < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                if nums[mid - 1] != target:
                    return mid
                else:
                    lb = lsearch(i, mid - 1)
                    return mid if lb == -1 else lb
            elif nums[mid] < target:
                i = mid + 1                                                
            else:
                j = mid - 1
        if nums[i] == target:
            return i
        elif i < len(nums) - 1 and nums[i + 1] == target:
            return i + 1
        else:
            return -1
    def rsearch(i: int, j: int) -> int:
        while (i + 1) < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                if nums[mid + 1] != target:
                    return mid
                else:
                    ub = rsearch(mid + 1, j)
                    return mid if ub == -1 else ub
            elif nums[mid] < target:
                i = mid + 1                                                 
            else:
                j = mid - 1
        if i < len(nums) - 1 and nums[i + 1] == target:
            return i + 1
        elif nums[i] == target:
            return i
        else:
            return -1

    if len(nums) < 1:
        return [-1, -1]
    return [lsearch(0, len(nums) - 1), rsearch(0, len(nums) - 1)]    

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(searchRange(nums, target))