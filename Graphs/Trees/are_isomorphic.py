from typing import Tuple, Dict, Set
import unittest

class graph(object):
    def __init__(self, n: int, adj_list:Dict[int, Set[int]]):
        self._n = n
        self.adj_list = adj_list

    def size(self)->int:
        return self._n

class TreeNode(object):
    def __init__(self, identifier, parent) -> None:
        super().__init__()
        self.Id = identifier
        self._parent = parent
        self._children = []

    def getChildren(self)->Tuple:
        return tuple(self._children)

    def addChild(self, child)->None:
        self._children.append(child)

def get_centers(g:graph)->Tuple[int]:
    leaves = set()
    degree = [0] * g.size()
    for v in range(g.size()):
        neighbours = g.adj_list.get(v)
        if neighbours is not None:
            degree[v] = len(neighbours)
        if degree[v] == 0 or degree[v] == 1: # don't use <= 1, because it could be -1 due to reduction of degree
            leaves.add(v)
            degree[v] = 0
    count = len(leaves)
    while count < g.size():
        new_leaves = set()
        for l in leaves:
            neighbours = g.adj_list.get(l)
            if neighbours is not None:
                for neighbour in neighbours:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 0 or degree[neighbour] == 1:
                        new_leaves.add(neighbour)
                        degree[neighbour] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return tuple(leaves)

def build_tree(g: graph, node: TreeNode, parent: TreeNode):
    children = g.adj_list.get(node.Id)
    if children is not None:
        for child in children:
            if parent is not None and child == parent.Id:
                continue # self-reference
            childNode = TreeNode(child, node)
            node.addChild(childNode)
            build_tree(g, childNode, node)

def root_tree(g: graph, rootId: int)->TreeNode:
    root = TreeNode(rootId, None)
    build_tree(g, root, None)
    return root

def encode(tree:TreeNode)->str:
    if tree is None:
        return ""
    children = tree.getChildren()
    if children is None:
        return "()"
    labels = []
    for child in children:
        labels.append(encode(child))
    
    sorted_labels = sorted(labels)
    return "(" + "".join(sorted_labels) + ")"

def are_isomorphic(g1: graph, g2: graph):
    centers1 = get_centers(g1)
    #print("tree1 centers:", centers1)
    centers2 = get_centers(g2)
    #print("tree2 centers:", centers2)
    g1_encodes = [None] * len(centers1)
    for i in range(len(centers1)):
        tree1 = root_tree(g1, centers1[i])
        g1_encodes[i] = encode(tree1)

    #print("Tree1 encodes", g1_encodes)
    for c2 in centers2:
        tree2 = root_tree(g2, c2)
        tree2_encode = encode(tree2)
        #print("tree2_encode", tree2_encode)
        for enc in g1_encodes:
            if enc == tree2_encode:
                return True        
    return False

class Tests(unittest.TestCase):
    def test_ex1(self):
        adj_list1 = dict()# adjacency list
        adj_list1[0] = {1}
        adj_list1[1] = {0, 2, 4}
        adj_list1[2] = {1}
        adj_list1[3] = {4, 5}
        adj_list1[4] = {1, 3}
        adj_list1[5] = {3}
        g1 = graph(6, adj_list1)

        adj_list2 = dict()# adjacency list
        adj_list2[0] = {1}
        adj_list2[1] = {0, 2}
        adj_list2[2] = {1, 4}
        adj_list2[3] = {4}
        adj_list2[4] = {2, 3, 5}
        adj_list2[5] = {4}
        g2 = graph(6, adj_list2)

        self.assertEqual(True, are_isomorphic(g1, g2))

    def test_ex2(self):
        adj_list1 = dict()# adjacency list
        adj_list1[0] = {1}
        adj_list1[1] = {0, 2, 4}
        adj_list1[2] = {1}
        adj_list1[3] = {4, 5}
        adj_list1[4] = {1, 3}
        adj_list1[5] = {3, 6}
        adj_list1[6] = {5}
        g1 = graph(7, adj_list1)

        adj_list2 = dict()# adjacency list
        adj_list2[0] = {1}
        adj_list2[1] = {0, 2}
        adj_list2[2] = {1, 4}
        adj_list2[3] = {4}
        adj_list2[4] = {2, 3, 5}
        adj_list2[5] = {4}
        g2 = graph(6, adj_list2)

        self.assertEqual(False, are_isomorphic(g1, g2))

if __name__ == "__main__":
    unittest.main(verbosity = 2)