'''
450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
'''

from binarytree import TreeNode

'''
parent = None
    node = root
    while node:
        if node.val == key:
            break
        else:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
    
    if node:
        # 3 cases
        if node.left and node.right: # two children exist
            # replace node with min. of right subtree or max. of left subtree
            min_parent = node
            min_node = node.right
            while min_node:
                if min_node.left:
                    min_parent = min_node
                    min_node = min_node.left
                else:
                    break
            if min_parent.left == min_node:
                min_parent.left = None
            else:
                min_parent.right = None            
            if parent:
                if parent.left == node:
                    parent.left = min_node
                else:
                    parent.right = min_node
            else:
                min_node.left = node.left
                min_node.right = None if min_node == node.right else node.right
                return min_node
        elif node.left or node.right: # only one child
            if parent:
                if parent.left == node:
                    parent.left = node.left if node.left else node.right
                else:
                    parent.right = node.left if node.left else node.right
            else: # root is the node
                return node.left if node.left else node.right
        else: # no children
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else: # root is the node
                return None
    return root
'''

'''
1. find node for corresponding key
2. if children exist, replace with appropriate child to satisy BST invariant
3. if no children, then dereference from parent
'''
def get_min_node(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node

def delete_node(root: TreeNode, key: int) -> TreeNode:
    if root is None:
        return None

    if root.val == key:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min_node = get_min_node(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, min_node.val)
    elif key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    return root