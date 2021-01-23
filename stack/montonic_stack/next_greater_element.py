'''
503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''
from typing import List

def next_greater_element(nums:List[int]) -> List[int]:
    if not nums or len(nums) < 1:
        return nums
    n = len(nums)
    result = [-1] * n
    ms = [] # decreasing stack; min at the bottom and max at the top
    for i in range(2*n - 1, -1, -1):
        j = i % n
        while ms and nums[ms[-1]] <= nums[j]:
            ms.pop(-1)
        result[j] = nums[ms[-1]] if ms else -1
        ms.append(j)
    return result

if __name__ == "__main__":
    print(next_greater_element([1,2,1]))
