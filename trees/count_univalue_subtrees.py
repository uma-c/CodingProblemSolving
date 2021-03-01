from binarytree import TreeNode

def _countUnivalSubTrees(node: TreeNode) -> int:
    if not node:
        return [0, None]

    if not node.left and not node.right:
        return [1, node.val]

    lc, rc = _countUnivalSubTrees(node.left), _countUnivalSubTrees(node.right)
    if (lc[1] and node.val == lc[1] and not rc[1]) or (rc[1] and node.val == rc[1] and not lc[1]) or (lc[1] == node.val and rc[1] == node.val):
        return [lc[0] + rc[0] + 1, node.val]
    else :
        return [lc[0] + rc[0], float("-inf")]

def countUnivalSubtrees(root: TreeNode) -> int:
    return _countUnivalSubTrees(root)[0]

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(1, None, TreeNode(5)))
    print(countUnivalSubtrees(root))