from list_node import ListNode

def oddEvenList(head: ListNode) -> ListNode:
    if not head or head.next is None:
        return head
    ol = olh = head
    el = elh = node = head.next
    while node:
        ol.next = node.next
        if ol.next:
            ol = ol.next
        if node.next:
            el.next = node.next.next
            el = el.next
            node = el
        else:
            node = None
    ol.next = elh
    return olh