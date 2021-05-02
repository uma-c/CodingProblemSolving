class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    def insert(node: TreeNode, parent: TreeNode) -> TreeNode:
        if node:
            if node.val > val:
                return insert(node.left, node)
            else:
                return insert(node.right, node)
        else:
            new_node = TreeNode(val)
            if parent:
                if parent.val < val:
                    parent.right = new_node
                else:
                    parent.left = new_node
            else:
                return new_node
    if root:
        insert(root, None)
        return root
    return insert(root, None)

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    new_node = TreeNode(val)
    if root:
        curr = root
        parent = None
        while curr:
            parent = curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        if parent.val < val:
            parent.right = new_node
        else:
            parent.left = new_node
        return root
    return new_node