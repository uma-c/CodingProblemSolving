'''
437. Path Sum III
Medium
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
from binarytree import TreeNode

def count_path_sum(tree:TreeNode, sum:int) -> int:
    if not tree:
        return 0

    return (1 if sum == tree.val else 0) + count_path_sum(tree.left, sum - tree.value) + count_path_sum(tree.right, sum - tree.value)

def path_sum(root:TreeNode, sum:int) -> int:
    if not root:
        return 0

    return count_path_sum(root, sum) + path_sum(root.left, sum) + path_sum(root.right, sum)