class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root: 'Node') -> int:
    def _maxDepth(node):
        d = 0
        if node:
            for c in node.children:
                d = max(d, _maxDepth(c))
            return d + 1
        return d
    return _maxDepth(root)