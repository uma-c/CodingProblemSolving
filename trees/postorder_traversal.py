from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def postorder(root: 'Node') -> List[int]:
    def _postorder(node):
        if node:
            for child in node.children:
                _postorder(child)
            result.append(node.val)
    result = []
    _postorder(root)
    return result