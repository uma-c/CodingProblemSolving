'''
659. Split Array into Consecutive Subsequences
Medium

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
'''
from typing import List
import collections

def can_split_into_consecutive_subseq(nums:List[int]) -> bool:
    counter = collections.Counter(nums)
    tails = collections.Counter()
    for num in nums:
        if counter[num] == 0:
            continue
        elif tails.get(num):
            tails[num] -= 1
            counter[num] -= 1
            if num + 1 in tails:
                tails[num + 1] += 1
            else:
                tails[num + 1] = 1
        elif counter.get(num + 1) and counter.get(num + 2):
            counter[num] -= 1
            counter[num + 1] -= 1
            counter[num + 2] -= 1
            if tails.get(num + 3):
                tails[num + 3] += 1
            else:
                tails[num + 3] = 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(can_split_into_consecutive_subseq([3,4,4,5,6,7,8,9,10,11]))