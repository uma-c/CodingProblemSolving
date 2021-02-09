from binarytree import TreeNode

def lca(root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    
    left_lca = lca(root.left, p, q)
    right_lca = lca(root.right, p, q)
    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    elif right_lca:
        return right_lca
    
    return None