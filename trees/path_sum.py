from binarytree import TreeNode

def _hasPathSum(node: TreeNode, r: int) -> bool:
    if not node:
        return False

    if not node.left and not node.right:
        return node.val == r

    return _hasPathSum(node.left, r - node.val) or _hasPathSum(node.right, r - node.val)

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    return _hasPathSum(root, targetSum)