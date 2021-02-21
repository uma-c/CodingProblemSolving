from list_node import ListNode

def insert(head: 'ListNode', insertVal: int) -> 'ListNode':
    '''    
    1) 1 -> 3 -> 4, 2
    2) 3 -> 4 -> 1 -> 2, 5
    3) 3 -> 4 -> 1 -> 2, 0
    4) 1 -> 2 -> 3, 4
    '''
    new_node = ListNode(insertVal)
    if not head:
        new_node.next = new_node
        return new_node
    node = head
    while node:
        if node.val <= insertVal <= node.next.val or (node.val > node.next.val and (insertVal >= node.val or insertVal <= node.next.val)) or node.next == head:
            temp = node.next
            node.next = new_node
            new_node.next = temp
            return head
        node = node.next