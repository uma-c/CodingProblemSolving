from binarytree import TreeNode
from typing import List, Dict
'''
[9, 3, 15, 20, 7]        [9, 15, 7, 20, 3]
 l  ^ r
'''

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def helper(in_left: int, in_right: int) -> TreeNode:
        if in_left > in_right:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        index = idx_map[val]        
        root.left = helper(in_left, index - 1)
        root.right = helper(index + 1, in_right)
        return root
    idx_map = {val : i for i, val in enumerate(inorder)}
    print(idx_map)
    return helper(0, len(inorder) - 1)

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(buildTree(preorder, inorder))