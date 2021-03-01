from binarytreenode import TreeNode

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    l, r = [], []
    if root.left:
        l.append(root.left)
    if root.right:
        r.append(root.right)
    while l or r:
        if len(l) != len(r):
            return False
        n = len(r)
        