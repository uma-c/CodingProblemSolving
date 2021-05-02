class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: TreeNode, key: int) -> TreeNode:
    def delete(node, val):
        if node:
            if node.val < val:
                node.right = delete(node.right, val)
            elif node.val > val:
                node.left = delete(node.left, val)
            else:
                if node.left and node.right:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.val= successor.val
                    node.right = delete(node.right, successor.val)
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            return node
        return None
    return delete(root, key)