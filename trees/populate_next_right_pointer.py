class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Node') -> 'Node':
    start_node = root
    while start_node:
        node = start_node
        prev = None
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
            node = node.next
        node = start_node
        start_node = None
        while node:
            if node.left:
                start_node = node.left
                break
            if node.right:
                start_node = node.right
                break
            node = node.next
    return root