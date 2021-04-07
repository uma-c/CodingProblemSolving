'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def isSameNode(n1: TreeNode, n2: TreeNode) -> bool:
        if not n1 and not n2:
            return True

        if not n1 or not n2:
            return False

        if n1.val != n2.val:
            return False

        return True

    stack = collections.deque()
    stack.append((p, q))
    while len(stack) > 0:
        n1, n2 = stack.popleft()
        if isSameNode(n1, n2):
            if n1 or n2:
                stack.append((n1.left if n1 else None, n2.left if n2 else None))
                stack.append((n1.right if n1 else None, n2.right if n2 else None))
        else:
            return False
    return True