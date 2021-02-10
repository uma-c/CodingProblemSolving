from binarytree import TreeNode
from typing import List
import unittest
import queue

def preorder_traversal(tree:TreeNode, result:List[int]):
    if tree is None:
        return

    result.append(tree.value)
    preorder_traversal(tree.left, result)
    preorder_traversal(tree.right, result)

def inorder_traversal(tree:TreeNode, result:List[int]):
    if tree is None:
        return
    
    inorder_traversal(tree.left, result)
    result.append(tree.value)
    inorder_traversal(tree.right, result)

def postorder_traversal(tree:TreeNode, result:List[int]):
    if tree is None:
        return
    
    postorder_traversal(tree.left, result)
    postorder_traversal(tree.right, result)
    result.append(tree.value)

def levelorder_traversal(tree:TreeNode, result:List[int]):
    if tree is None:
        return
    
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        t = q.get()        
        result.append(t.value)
        if t.left is not None:
            q.put(t.left)
        if t.right is not None:
            q.put(t.right)

class Tests(unittest.TestCase):
    def test_preorder_traversal(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = []
        preorder_traversal(root, result)
        self.assertEqual([1,2,3], result)

    def test_inorder_traversal(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = []
        inorder_traversal(root, result)
        self.assertEqual([2,1,3], result)

    def test_postorder_traversal(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = []
        postorder_traversal(root, result)
        self.assertEqual([2,3,1], result)

    def test_levelorder_traversal(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        result = []
        levelorder_traversal(root, result)
        self.assertEqual([1,2,3,4,5,6,7], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)


    

