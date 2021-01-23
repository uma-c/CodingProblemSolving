'''
1658. Minimum Operations to Reduce X to Zero
Medium
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
'''

from typing import List

# Space complexity: O(1), Time Complexity: O(n)
def min_operations_to_0(nums:List[int], x:int) -> int:
    n = len(nums)
    nums_sum = sum(nums)    
    if nums_sum < x:
        return -1
    elif nums_sum == x:
        return n
       
    t = nums_sum - x 
    i = 0
    nt = -1
    sub_sum = 0
    for j in range(n):
        sub_sum += nums[j]
        while sub_sum > t and i < j:
            sub_sum -= nums[i]
            i += 1
        if sub_sum == t:
            nt = max(nt, j - i + 1)
    return (n - nt) if nt != -1 else -1

# Space complexity: O(n)
def min_operations_to_0_1(nums:List[int], x:int) -> int:
    n = len(nums)
    l_ops_sum_map = dict()
    l_ops_sum_map[0] = 0
    l, l_sum = 0, 0
    min_ops = float("inf")
    while l_sum <= x and l < n:   
        l_sum += nums[l]  
        l += 1   
        if l_sum == x:
            min_ops = l        
        l_ops_sum_map[l_sum] = l

    r, r_sum = 0, 0
    while r_sum <= x and r < n:
        r_sum += nums[n - r - 1]
        r += 1
        diff = x - r_sum
        if diff in l_ops_sum_map and (l_ops_sum_map[diff] + r) < n:
            min_ops = min(min_ops, l_ops_sum_map[diff] + r)
        
    return min_ops if min_ops != float("inf") else -1
    

if __name__ == "__main__":
    print(min_operations_to_0([1,1,4,2,3], 5))
    print(min_operations_to_0([5,6,7,8,9], 4))
    print(min_operations_to_0([1,1], 3))