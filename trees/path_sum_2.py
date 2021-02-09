'''
113. Path Sum II
Medium
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

from binarytree import TreeNode
from typing import List

def path_to_sum(node: TreeNode, t: int, path: List[int], ans:List[List[int]]) -> bool:
    if not node:
        return

    if not node.left and not node.right:
        if node.val == t:
            ans.append(path + [node.val])
        return
    
    path_to_sum(node.left, t - node.val, path+[node.val], ans)
    path_to_sum(node.right, t - node.val, path+[node.val], ans)

def get_paths_for_sum(root: TreeNode, targetSum: int) -> List[List[int]]:
    ans = []
    path_to_sum(root, targetSum, [], ans)
    return ans