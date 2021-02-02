'''
268. Missing Number
Easy
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''
from typing import List

def missing_2_numbers(nums:List[int]) -> List[int]:
    result = 2 * len(nums) + 1
    for i, num in enumerate(nums):
        result += i - num
    pivot = result // 2
    leftXor = 0
    for i in range(1, pivot + 1):
        leftXor ^= i

    rightXor = 0
    for i in range(pivot + 1, len(nums) + 2):
        rightXor ^= i

    leftNumXor, rightNumXor = 0, 0
    for num in nums:
        if num <= pivot:
            leftNumXor ^= num
        else:
            rightNumXor ^= num
    return [leftXor ^ leftNumXor, rightXor ^ rightNumXor]

def missing_number(nums:List[int]) -> int:
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i
        result ^= num
    return result

def missing_number1(nums:List[int]) -> int:
    result = len(nums)
    for i, num in enumerate(nums):
        result += i - num
    return result

if __name__ == '__main__':
    #print(missing_number([3, 0, 1]))
    print(missing_2_numbers([0,1,2,3,4,5]))