'''
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
from typing import List


'''
Core idea: 
water[i] = min(l_max, r_max) - height[i]
where l_max = max(0..i), r_max = max(i..n)
'''

'''
Time complexity: O(N^2), Space complexity: O(1)
'''
def trap1(height:List[int]) -> int:
    count = 0
    for i in range(1, len(height) - 1):
        l_max = max(height[:(i+1)])
        r_max = max(height[i:])
        count += min(l_max, r_max) - height[i]
    return count

def trap(height:List[int]) -> int:
    count = 0
    l, r = 0, len(height) - 1
    l_max, r_max = 0, 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= l_max:
                l_max = height[l]
            else:
                count += l_max - height[l]
            l += 1
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                count += r_max - height[r]
            r -= 1
    return count

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))