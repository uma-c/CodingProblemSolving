from binarytree import TreeNode

def _isSymmetric(left: TreeNode, right: TreeNode) -> bool:
    if not left and not right:
        return True
    elif (left and not right) or (not left and right) or left.val != right.val:
        return False

    return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    return _isSymmetric(root.left, root.right)