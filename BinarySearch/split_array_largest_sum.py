'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
'''

from typing import List

def splitArray(nums: List[int], m: int) -> int:
    def possible(s: int) -> bool:
        ss, count = 0, 1
        for num in nums:
            ss += num
            if ss > s:
                ss = num
                count += 1
                if count > m:
                    return False
        return True
    n = len(nums)
    if m == 1:
        return sum(nums)
    if m == n:
        return max(nums)
    hi = lo = 0
    for num in nums:
        if num > lo:
            lo = num
        hi += num
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if possible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    nums = [7,2,5,10,8]
    m = 2
    print(splitArray(nums, m))