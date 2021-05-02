class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def nextLowestNode(node: 'TreeNode'):
    while node.left:
        node = node.left
    return node

def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    def _inorderSuccessor(node, stack_of_parents):
        if node.val < p.val:
            stack_of_parents.append(node)
            return _inorderSuccessor(node.right, stack_of_parents)
        elif node.val > p.val:
            stack_of_parents.append(node)
            return _inorderSuccessor(node.left, stack_of_parents)
        else:
            if node.right:
                return nextLowestNode(root.right)
            else:
                if stack_of_parents:
                    parent = stack_of_parents[-1]
                    if parent.left == node:
                        return parent
                    else:
                        n = node
                        found = False
                        while stack_of_parents:
                            parent = stack_of_parents.pop()
                            if n != parent.right:
                                found = True
                                break
                            n = parent
                        if found:
                            return nextLowestNode(parent.right)                        
                        return None
    return _inorderSuccessor(root, [])