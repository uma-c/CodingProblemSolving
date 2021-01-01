'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
 

Constraints:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
0 <= i <= j <= nums.length - 1
'''
from typing import List
import unittest

class TreeNode:
    def __init__(self, s, e, val):
        self.s = s
        self.e = e
        self.value = val
        self.left = None
        self.right = None

def buildTree(nums: List[int], s: int, e: int) -> TreeNode:
    if s > e or e > len(nums) or s < 0:
        raise ValueError('invalid input')
    if s == e:
        return TreeNode(s, e, nums[s])

    m = s + (e - s) // 2
    left = buildTree(nums, s, m)
    right = buildTree(nums, m + 1, e)
    node = TreeNode(s, e, left.value + right.value)
    node.left = left
    node.right = right
    return node

def rangeQuery(root: TreeNode, i : int, j : int, s : int, e : int) -> int:
    if s == i and e == j:
        return root.value if root else 0
    m = s + (e - s) // 2
    if j <= m:
        return rangeQuery(root.left, i, j, s, m)
    elif i > m:
        return rangeQuery(root.right, i, j, m + 1, e)
    else:
        return rangeQuery(root.left, i, m, s, m) + rangeQuery(root.right, m + 1, j, m + 1, e)


def update(root: TreeNode, s: int, e: int, i: int, val: int) -> None:
    if s == e == i:
        root.value = val
        return
    m = s + (e - s) // 2
    if i <= m:
        update(root.left, s, m, i, val)
    else:
        update(root.right, m + 1, e, i, val)
    root.value = root.left.value + root.right.value

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [1, 3, 5]
        root = buildTree(nums, 0, len(nums) - 1)
        sum_0_2 = rangeQuery(root, 0, 2, 0, len(nums) - 1)
        self.assertEqual(9, sum_0_2)
        update(root, 0, len(nums) - 1, 2, 4)
        sum_0_2 = rangeQuery(root, 0, 2, 0, len(nums) - 1)
        self.assertEqual(8, sum_0_2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
