# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def height_balanced(tree:TreeNode) -> int:
        if not tree:
            return True, -1

        isLeftHeightBalanced, leftHeight = height_balanced(tree.left)
        if not isLeftHeightBalanced:
            return False, 0
        
        isRightHeightBalanced, rightHeight = height_balanced(tree.right)
        if not isRightHeightBalanced:
            return False, 0
        
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
    
    return height_balanced(root)[0]