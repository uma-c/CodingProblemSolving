from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    def _sortedArrayToBST(i:int, j: int) -> TreeNode:
        if i > j:
            return None
        if i == j:
            return TreeNode(nums[i])
        m = i + (j - i) // 2
        return TreeNode(nums[m], _sortedArrayToBST(i, m - 1), _sortedArrayToBST(m + 1, j))
    return _sortedArrayToBST(0, len(nums) - 1)