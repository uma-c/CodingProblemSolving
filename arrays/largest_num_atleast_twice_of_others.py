'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
 

Hint #1  
Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`. Scan through the array again. If we find some `x != m` with `m < 2*x`, we should return `-1`. Otherwise, we should return `maxIndex`.
'''

from typing import List

def dominantIndex(nums: List[int]) -> int:
    max1_i, max1, max2 = -1, float("-inf"), float("-inf")
    for i, v in enumerate(nums):
        if v > max1:
            max2 = max1
            max1 = v
            max1_i = i
        if max2 < v and max1 > v:
            max2 = v
    if max1 >= 2 * max2:
        return max1_i
    return -1

if __name__ == "__main__":
    nums = [0,0,2,3]
    print(dominantIndex(nums))