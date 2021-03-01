from binarytree import TreeNode
from typing import List, Dict
'''
[9, 3, 15, 20, 7]        [9, 15, 7, 20, 3]
 l  ^ r
'''

def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(in_left: int, in_right: int) -> TreeNode:
        if in_left > in_right:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        index = idx_map[val]
        root.right = helper(index + 1, in_right)
        root.left = helper(in_left, index - 1)
        return root
    idx_map = {val : i for i, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(buildTree(inorder, postorder))