'''
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
from typing import List

'''
sum[j] - sum[i] = k
sum[i] = sum[j] - k
'''
def subarrays_sum_k(nums:List[int], k:int):
    sub_sums_map = {0 : 1}
    sub_sum = 0
    count = 0
    for num in nums:
        sub_sum += num
        count += sub_sums_map.get(sub_sum - k, 0)            
        sub_sums_map[sub_sum] = sub_sums_map.get(sub_sum, 0) + 1
    return count

if __name__ == "__main__":
    print(subarrays_sum_k([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2], 22))