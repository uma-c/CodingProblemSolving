'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
'''
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root: TreeNode) -> List[TreeNode]:
    trees = collections.defaultdict()
    trees.default_factory = trees.__len__
    count = collections.Counter()
    ans = []
    def lookup(node):
        if node:
            uid = trees[node.val, lookup(node.left), lookup(node.right)] # serialize
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid
    lookup(root)
    return ans
    