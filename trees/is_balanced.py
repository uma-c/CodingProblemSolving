'''
difference in height of subtrees should not be more than 1 
'''
from binarytree import TreeNode

def height_balanced(tree:TreeNode) -> int:
    if not tree:
        return [True, 0]
    
    hbl = height_balanced(tree.left)
    hbr = height_balanced(tree.right)
    return [hbl[0] and hbr[0] and abs(hbl[1] - hbr[1]) <= 1, max(hbl[1], hbr[1]) + 1]

def is_balanced(root:TreeNode) -> bool:
    return height_balanced(root)[0]