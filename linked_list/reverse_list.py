from list_node import ListNode

def reverse_list(head:ListNode) -> ListNode:
    if not head:
        return head
    prev = head
    curr = head.next
    prev.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev