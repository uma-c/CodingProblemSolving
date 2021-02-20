from list_node import ListNode

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(None, head)
    prev = dummy
    node = dummy.next
    while node:
        if node.val != val:
            temp = node.next
            prev = node
            node = temp            
        else:
            temp = node.next
            prev.next = temp
            node.next = None
            node = temp
    return dummy.next