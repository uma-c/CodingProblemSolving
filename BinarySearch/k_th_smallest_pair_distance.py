'''
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
from typing import List

def smallestDistancePair(nums: List[int], k: int) -> int:
    def is_kth_distance(d: int):
        count = left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > d:
                left += 1
            count += right - left
        return count >= k

    nums.sort()
    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = l + (r - l) // 2
        if is_kth_distance(m):
            r = m
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    nums = [1, 3, 1]
    k = 1
    print(smallestDistancePair(nums, k))