'''
114. Flatten Binary Tree to Linked List
Medium

Given the root of a binary tree, flatten it to a linked list in-place.

 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''
from binarytree import TreeNode

def _flatten(subtree:TreeNode, parent:TreeNode) -> TreeNode:
    if subtree is None:
        return parent

    l = subtree.left
    r = subtree.right
    subtree.left = subtree.right = None
    parent.right = subtree
    p = _flatten(l, subtree)
    return _flatten(r, p)

def flatten(root:TreeNode) -> None:
    l = root.left
    r = root.right
    root.left = root.right = None
    p = _flatten(l, root)
    _flatten(r, p)        

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6)))
    flatten(root)
    print(root)