'''
645. Set Mismatch
Easy
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''

from typing import List

'''
Core idea: Mark number as negative for the index of a number
to find dup and missing number
'''
def find_error_nums(nums:List[int]) -> List[int]:
    dup = None
    missing = None
    for i in range(len(nums)):        
        idx = nums[i] - 1 if nums[i] > 0 else -nums[i] - 1
        if nums[idx] < 0:
            dup = idx + 1
        else:
            nums[idx] = -nums[idx]
    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            return [dup, missing]
    return [dup, missing]

if __name__ == "__main__":
    # [2, -2]
    # 2 - 1
    print(find_error_nums([2, 2]))