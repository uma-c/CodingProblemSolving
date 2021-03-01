from typing import List
from binarytreenode import TreeNode
import collections

def preorderTraversal(root: TreeNode) -> List[int]:
    '''
    node
    node.left
    node.right
    '''
    if not root:
        return root
    path, stack = [], [[root, False]]
    while len(stack) > 0:
        node, visited = stack.pop()                
        if visited:
            path.append(node.val)
        else:
            if node.right:
                stack.append([node.right, False])
            if node.left:
                stack.append([node.left, False])            
            stack.append([node, True])
    return path

def inorderTraversal(root: TreeNode) -> List[int]:
    '''
    node.left
    node
    node.right
    '''
    if not root:
        return root
    path, stack = [], [[root, False]]
    while len(stack) > 0:
        node, visited = stack.pop()                
        if visited:
            path.append(node.val)
        else:
            if node.right:
                stack.append([node.right, False])
            stack.append([node, True])
            if node.left:
                stack.append([node.left, False])
    return path

def postorderTraversal(root: TreeNode) -> List[int]:
    '''
    node
    node.left
    node.right
    '''
    if not root:
        return root
    path, stack = [], [[root, False]]
    while len(stack) > 0:
        node, visited = stack.pop()                
        if visited:
            path.append(node.val)
        else:            
            stack.append([node, True])
            if node.right:
                stack.append([node.right, False])
            if node.left:
                stack.append([node.left, False])
    return path

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return root
    nodes = [root]
    path = []
    while nodes:
        vals = []
        children = []
        for node in nodes:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            vals.append(node.val)
        nodes = children
        path.append(vals)
    return path