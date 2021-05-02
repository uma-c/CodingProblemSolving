from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root: 'Node') -> List[int]:
    def _preorder(node):
        if node:
            result.append(node.val)
            for child in node.children:
                _preorder(child)    
    result = []
    _preorder(root)
    return result