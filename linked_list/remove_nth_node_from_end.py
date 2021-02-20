from list_node import ListNode

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    r = head
    while n > 1:
        n -= 1
        r = r.next
    l = head
    prev = None
    while r.next:
        prev = l
        l = l.next
        r = r.next
    if prev:
        prev.next = l.next
        l.next = None
        return head
    else:
        temp = l.next
        l.next = None
        return temp
