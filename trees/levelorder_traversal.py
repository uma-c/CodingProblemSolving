from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root:
        result = [root.val]
        lvl = [root]
        while lvl:
            c_level_nodes = []
            c_level_vals = []
            parents = lvl.pop()
            for p in parents:
                for child in p.children:
                    c_level_nodes.append(child)
                    c_level_vals.append(child.val)
            lvl = c_level_nodes
            result.append(c_level_vals)
        return result
    return []