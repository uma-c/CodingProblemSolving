# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def _flatten(head: 'Node') -> 'Node':
    if not head:
        return head
    node = tail = head
    while node:       
        temp = node.next               
        if not temp:
            tail = node
        if node.child:
            chead = node.child
            node.child = None
            tail = ctail = _flatten(chead)
            node.next = chead
            chead.prev = node
            ctail.next = temp            
            if temp:
                temp.prev = ctail 
        node = temp
    return tail

def flatten(head: 'Node') -> 'Node':
    node = head
    _flatten(node)
    return head
        