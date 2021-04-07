'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

from typing import List

class TreeNode:
    def __init__(self, s, e, val, nums):
        self.s = s
        self.e = e
        self.value = val
        self.left = None
        self.right = None
        self.nums = nums

def build_min_segment_tree(nums: List[int]) -> TreeNode:
    def build_tree(s: int, e: int) -> TreeNode:
        if s == e:
            return TreeNode(s, e, s, nums)
        m = s + (e - s) // 2
        left_subtree = build_tree(s, m)
        right_subtree = build_tree(m + 1, e)
        min_idx = left_subtree.value if nums[left_subtree.value] <= nums[right_subtree.value] else right_subtree.value
        root = TreeNode(s, e, min_idx, nums)
        root.left = left_subtree
        root.right = right_subtree
        return root
    return build_tree(0, len(nums) - 1)

def range_min_query(root: TreeNode, i: int, j: int) -> int:
    if root.s == i and root.e == j:
        return root.value
    m = root.s + (root.e - root.s) // 2
    if j <= m:
        return range_min_query(root.left, i, j)
    elif i > m:
        return range_min_query(root.right, i, j)
    else:
        nums = root.nums
        left_min_idx = range_min_query(root.left, i, m)
        right_min_idx = range_min_query(root.right, m + 1, j)
        return left_min_idx if nums[left_min_idx] <= nums[right_min_idx] else right_min_idx

def largestRectangleArea(heights: List[int]) -> int:
    min_st = build_min_segment_tree(heights)
    def largest_rectangle_area(i: int, j: int) -> int:
        if i == j:
            return heights[i]
        min_rect_idx = range_min_query(min_st, i, j)
        left_area = largest_rectangle_area(i, min_rect_idx - 1) if min_rect_idx > i  else float("-inf")
        right_area = largest_rectangle_area(min_rect_idx + 1, j) if j > min_rect_idx else float("-inf")
        i_j_area = heights[min_rect_idx] * (j - i + 1)
        return max(left_area, right_area, i_j_area)        
    return largest_rectangle_area(0, len(heights) - 1)

def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    stack = []
    max_area = 0

    for i in range(n):
        if not stack or stack[-1][0] < heights[i]:
            stack.append((heights[i], i))
        elif stack[-1][0] == heights[i]:
            continue
        else:
            while stack:
                if stack[-1][0] > heights[i]:
                    value, index = stack.pop()
                    area = (i - index) * value
                    if area > max_area:
                        max_area = area
                else:
                    break
            stack.append((heights[i], index))

    while stack:
        value, index = stack.pop()
        area = (n - index) * value
        if area > max_area:
            max_area = area
    return max_area

if __name__ == "__main__":
    heights = [2, 4]#[2,1,5,6,2,3]#[6, 4, 5, 2, 4, 3, 9]
    # min_st = build_min_segment_tree(heights)
    # print(range_min_query(min_st, 0, 7))
    print(largestRectangleArea(heights))