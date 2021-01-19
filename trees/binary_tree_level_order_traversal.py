'''
102. Binary Tree Level Order Traversal
Medium

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from binarytree import TreeNode
from typing import List

def level_order_traversal(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    result = [[root.value]]
    level = [root]
    while level:
        new_level = []
        new_level_vals = []
        for node in level:
            if node.left:
                new_level.append(node.left)
                new_level_vals.append(node.left.value)
            if node.right:
                new_level.append(node.right)
                new_level_vals.append(node.right.value)
        level = new_level
        if new_level_vals:
            result.append(new_level_vals)
    return result