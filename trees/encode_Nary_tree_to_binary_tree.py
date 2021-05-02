from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Codec:
    def encode(self, root:'Node') -> TreeNode:
        def toListNode(lst:List[Node]) -> ListNode:
            if lst:
                list_node = head = ListNode()
                for item in lst:
                    list_node.next = ListNode(self.encode(item))
                    list_node = list_node.next
                return head.next
        if root:    
            root_tree_node = TreeNode(toListNode([root]))
            if root.children:
                root_tree_node.left = TreeNode(toListNode(root.children))
            return root_tree_node

    def decode(self, root: 'TreeNode') -> Node:
        root_node = Node(root.val.val) if root.val else None
        if root_node and root.left:
            children = []
            node = root.left
            while node:
                children.append(self.decode(node))
                node = node.next
            root_node.children = children
        return root_node
            
                