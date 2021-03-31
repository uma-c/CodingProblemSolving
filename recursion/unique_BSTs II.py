'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
1 2 3
rv = 1, l = 0, r = 2
'''
'''
Catalan Number
C(n) = (2n)!/((n + 1)! * n!)
'''
import math

def numberOfTrees(n: int) -> int:
    n_factorial = math.factorial(n)
    return math.factorial(2 * n) // ((n + 1) * n_factorial * n_factorial)

def generateTrees(n: int) -> List[TreeNode]:
    def _generateTrees(i:int, j:int) -> List[TreeNode]:
        if i > j:
            return [None]
        if i == j:
            return [TreeNode(i)]
        trees = []
        for k in range(i, j + 1):            
            left_trees = _generateTrees(i, k - 1) 
            right_trees = _generateTrees(k + 1, j)            
            for lt in left_trees:
                for rt in right_trees:
                    trees.append(TreeNode(k, lt, rt))
        return trees
    return _generateTrees(1, n)

if __name__ == "__main__":
    trees = generateTrees(3)
    print(len(trees))