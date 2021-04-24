'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10**4
arr is sorted in ascending order.
-10**4 <= arr[i], x <= 10**4
'''
from typing import List
import bisect

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    if arr[0] > x:
        return arr[:k]
    elif arr[-1] < x:
        return arr[len(arr) - k:]
    else:
        lo_i = bisect.bisect_left(arr, x)
        lo_i = 0 if lo_i < k else lo_i - k
        hi_i = lo_i + 2 * k        
        if hi_i >= len(arr):
            hi_i = len(arr) - 1
        while (hi_i - lo_i) >= k:
            if abs(arr[lo_i] - x) > abs(arr[hi_i] - x):
                lo_i += 1
            else:
                hi_i -= 1
        return arr[lo_i:hi_i + 1]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    print(findClosestElements(arr, k, x))