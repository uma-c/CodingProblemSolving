'''
487 Max Consecutive Ones II
Problem:

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''
from typing import List

def max_consecutive_ones(nums:List[int]) -> int:
    max1s = 0
    last_streak, last_zero = 0, -1
    for i in range(len(nums)):
        if not nums[i]:
            streak = i if last_zero < 0 else (i - last_zero - 1)
            max1s = max(max1s, last_streak + streak + 1)
            last_streak = streak
            last_zero = i
    streak = len(nums) if last_zero < 0 else (len(nums) - last_zero - 1)
    max1s = max(max1s, last_streak + streak + (0 if last_zero < 0 else 1))
    return max1s

if __name__ == "__main__":
    #nums = [1,0,1,1,0]
    #nums = [1,1,1,1,0]
    #nums = [0,1,1,1,1,0]
    nums = [1, 1, 0, 1]
    print(max_consecutive_ones(nums))