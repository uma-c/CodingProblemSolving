'''
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
'''

from binarytree import TreeNode

def _is_valid_bst(node: TreeNode, min_node: TreeNode, max_node: TreeNode) -> bool:
    if node is None:
        return True

    if min_node and min_node.value >= node.value:
        return False

    if max_node and max_node.value <= node.value:
        return False

    return _is_valid_bst(node.left, min_node, node) and _is_valid_bst(node.right, node, max_node)

def is_valid_bst(root: TreeNode) -> bool:
    return _is_valid_bst(root, None, None)